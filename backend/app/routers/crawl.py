import asyncio
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Event, EventTitle, EventDescription, EventLocation, EventSource, EventMedia, EventPerspective
from ..schemas import EventCreate

router = APIRouter(prefix="/api/crawl", tags=["crawl"])


class CrawlRequest(BaseModel):
    source: str = "wikipedia"
    lang: str = "en"
    topic: str = "History of the People's Republic of China"
    max_events: int = 50


@router.post("/start")
async def start_crawl(request: CrawlRequest, db: Session = Depends(get_db)):
    if request.source == "wikipedia":
        from ..crawler.wikipedia import crawl_wikipedia_topic

        events = await crawl_wikipedia_topic(request.topic, request.lang, max_events=request.max_events)
        count = 0
        for ev_data in events:
            title_val = ev_data.get("title", "")
            existing = (
                db.query(Event)
                .join(EventTitle)
                .filter(EventTitle.language == request.lang, EventTitle.title == title_val)
                .first()
            )
            if existing:
                continue

            event = Event(
                date=ev_data.get("date", date.today()),
                date_end=ev_data.get("date_end"),
                date_precision=ev_data.get("date_precision", "day"),
                category=ev_data.get("category"),
                tags=ev_data.get("tags", []),
                importance=ev_data.get("importance", 0),
                wiki_qid=ev_data.get("wiki_qid"),
            )
            db.add(event)
            db.flush()

            db.add(
                EventTitle(event_id=event.id, language=request.lang, title=title_val)
            )
            summary = ev_data.get("summary") or ev_data.get("description") or ""
            db.add(
                EventDescription(event_id=event.id, language=request.lang, summary=summary)
            )

            loc = ev_data.get("location")
            if loc and isinstance(loc, dict):
                existing_loc = db.query(EventLocation).filter(EventLocation.event_id == event.id).first()
                if not existing_loc:
                    db.add(
                        EventLocation(
                            event_id=event.id,
                            lat=loc.get("lat"),
                            lng=loc.get("lng"),
                            country=loc.get("country"),
                            names=loc.get("names", {}),
                        )
                    )

            src_url = ev_data.get("source_url")
            if src_url:
                existing_src = db.query(EventSource).filter(EventSource.event_id == event.id, EventSource.url == src_url).first()
                if not existing_src:
                    db.add(
                        EventSource(
                            event_id=event.id,
                            language=request.lang,
                            url=src_url,
                            publisher="Wikipedia",
                            reliability=0.8,
                        )
                    )

            image_url = ev_data.get("image_url")
            if image_url:
                db.add(
                    EventMedia(
                        event_id=event.id,
                        media_type="photo",
                        url=image_url,
                    )
                )

            count += 1

        db.commit()
        return {"source": request.source, "lang": request.lang, "events_imported": count}

    elif request.source == "wikipedia_crosslang":
        from ..crawler.wikipedia import crawl_wikipedia_topic, correlate_events_via_wikidata

        all_lang_events = {}
        for lang in ["zh_tw", "en", "ja", "ko"]:
            lang_events = await crawl_wikipedia_topic(request.topic, lang, max_events=request.max_events // 4)
            all_lang_events[lang] = lang_events
            print(f"[crosslang] {lang}: {len(lang_events)} events")

        correlated = await correlate_events_via_wikidata(all_lang_events)
        count = 0
        for ev_data in correlated:
            title_val = ev_data.get("title", "")
            src_lang = ev_data.get("_lang", request.lang)
            existing = (
                db.query(Event)
                .join(EventTitle)
                .filter(EventTitle.language == src_lang, EventTitle.title == title_val)
                .first()
            )
            if existing:
                continue

            event = Event(
                date=ev_data.get("date", date.today()),
                date_end=ev_data.get("date_end"),
                date_precision=ev_data.get("date_precision", "day"),
                category=ev_data.get("category"),
                tags=ev_data.get("tags", []),
                importance=ev_data.get("importance", 0),
                wiki_qid=ev_data.get("wiki_qid"),
            )
            db.add(event)
            db.flush()

            db.add(EventTitle(event_id=event.id, language=src_lang, title=title_val))
            title_by_lang = ev_data.get("title_by_lang", {})
            for t_lang, t_title in title_by_lang.items():
                if t_lang != src_lang:
                    db.add(EventTitle(event_id=event.id, language=t_lang, title=t_title))

            summary = ev_data.get("summary") or ""
            db.add(EventDescription(event_id=event.id, language=src_lang, summary=summary))

            src_url = ev_data.get("source_url")
            if src_url:
                db.add(
                    EventSource(
                        event_id=event.id,
                        language=src_lang,
                        url=src_url,
                        publisher="Wikipedia",
                        reliability=0.8,
                    )
                )
            count += 1

        db.commit()
        return {"source": "wikipedia_crosslang", "events_imported": count, "languages": 4}

    elif request.source == "news":
        from ..crawler.news_crawlers import crawl_all_news_sources, fetch_article_perspective

        articles = await crawl_all_news_sources(request.topic, max_per_source=10)
        count = 0
        for article in articles:
            existing = (
                db.query(Event)
                .join(EventTitle)
                .filter(EventTitle.title == article.get("title", "")[:200])
                .first()
            )
            if existing:
                continue

            perspective_data = await fetch_article_perspective(article["url"], article["source"])

            event = Event(
                date=date.today(),
                date_precision="year",
                category=None,
                tags=[request.topic, article["source"]],
                importance=30,
            )
            db.add(event)
            db.flush()

            db.add(
                EventTitle(event_id=event.id, language=article["lang"], title=article.get("title", "")[:200])
            )
            if perspective_data and perspective_data.get("content"):
                db.add(
                    EventDescription(
                        event_id=event.id,
                        language=article["lang"],
                        summary=perspective_data["content"][:1000],
                    )
                )

            db.add(
                EventSource(
                    event_id=event.id,
                    language=article["lang"],
                    url=article["url"],
                    publisher=article["source"],
                    reliability=0.6,
                )
            )

            db.add(
                EventPerspective(
                    event_id=event.id,
                    country_code=article.get("country", ""),
                    language=article["lang"],
                    viewpoint=perspective_data.get("content", "")[:1000] if perspective_data else "",
                    source_url=article["url"],
                )
            )

            count += 1

        db.commit()
        return {"source": "news", "topic": request.topic, "articles_imported": count}

    raise HTTPException(status_code=400, detail=f"Unknown source: {request.source}")
