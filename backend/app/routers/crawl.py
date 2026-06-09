import asyncio
from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Event, EventTitle, EventDescription, EventLocation, EventSource
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
            existing = (
                db.query(Event)
                .join(EventTitle)
                .filter(EventTitle.language == request.lang, EventTitle.title == ev_data.get("title"))
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
            )
            db.add(event)
            db.flush()

            db.add(
                EventTitle(event_id=event.id, language=request.lang, title=ev_data.get("title", ""))
            )
            summary = ev_data.get("summary") or ev_data.get("description") or ""
            db.add(
                EventDescription(event_id=event.id, language=request.lang, summary=summary)
            )

            loc = ev_data.get("location")
            if loc and isinstance(loc, dict):
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
                db.add(
                    EventSource(
                        event_id=event.id,
                        language=request.lang,
                        url=src_url,
                        publisher="Wikipedia",
                        reliability=0.8,
                    )
                )
            count += 1

        db.commit()
        return {"source": request.source, "lang": request.lang, "events_imported": count}

    raise HTTPException(status_code=400, detail=f"Unknown source: {request.source}")
