from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from ..database import get_db
from ..models import Event, EventTitle, EventDescription, EventLocation
from ..schemas import (
    EventCreate,
    EventDetail,
    EventListItem,
    EventUpdate,
    GeoFeature,
)

router = APIRouter(prefix="/api/events", tags=["events"])


def _event_to_list_item(event: Event) -> dict:
    return {
        "id": event.id,
        "date": event.date.isoformat(),
        "date_end": event.date_end.isoformat() if event.date_end else None,
        "date_precision": event.date_precision,
        "category": event.category,
        "tags": event.tags or [],
        "importance": event.importance,
        "titles": [
            {"id": t.id, "event_id": t.event_id, "language": t.language, "title": t.title}
            for t in event.titles
        ],
        "descriptions": [
            {"id": d.id, "event_id": d.event_id, "language": d.language, "summary": d.summary, "content": d.content}
            for d in event.descriptions
        ],
        "location": (
            {
                "id": event.location.id,
                "event_id": event.location.event_id,
                "lat": event.location.lat,
                "lng": event.location.lng,
                "country": event.location.country,
                "names": event.location.names or {},
            }
            if event.location
            else None
        ),
        "source_count": len(event.sources),
    }


@router.get("")
def list_events(
    lang: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    country: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
    importance_min: Optional[int] = Query(None),
    limit: int = Query(100, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    query = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
        joinedload(Event.sources),
    )

    if category:
        query = query.filter(Event.category == category)
    if date_from:
        query = query.filter(Event.date >= date_from)
    if date_to:
        query = query.filter(Event.date <= date_to)
    if importance_min is not None:
        query = query.filter(Event.importance >= importance_min)
    if q:
        search_term = f"%{q}%"
        query = query.join(EventTitle).filter(
            or_(
                EventTitle.title.ilike(search_term),
                EventDescription.summary.ilike(search_term),
                EventDescription.content.ilike(search_term),
            )
        ).distinct()
    if lang:
        query = query.join(EventTitle).filter(EventTitle.language == lang).distinct()

    total = query.count()
    events = query.order_by(Event.date.asc(), Event.importance.desc()).offset(offset).limit(limit).all()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "events": [_event_to_list_item(e) for e in events],
    }


@router.get("/geo")
def geo_events(
    lang: str = Query("en"),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Event).options(joinedload(Event.titles), joinedload(Event.location))

    if date_from:
        query = query.filter(Event.date >= date_from)
    if date_to:
        query = query.filter(Event.date <= date_to)
    if category:
        query = query.filter(Event.category == category)

    events = query.filter(Event.location.has()).all()

    features = []
    for e in events:
        if e.location and e.location.lat and e.location.lng:
            title_match = [t for t in e.titles if t.language == lang]
            title = title_match[0].title if title_match else (e.titles[0].title if e.titles else "Untitled")
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [e.location.lng, e.location.lat],
                },
                "properties": {
                    "event_id": e.id,
                    "title": title,
                    "date": e.date.isoformat(),
                    "category": e.category,
                    "names": e.location.names or {},
                },
            })

    return {"type": "FeatureCollection", "features": features}


@router.get("/categories")
def list_categories(db: Session = Depends(get_db)):
    results = db.query(Event.category).distinct().filter(Event.category.isnot(None)).all()
    return [r[0] for r in results if r[0]]


@router.get("/languages")
def list_languages(db: Session = Depends(get_db)):
    results = db.query(EventTitle.language).distinct().all()
    return sorted(set(r[0] for r in results if r[0]))


@router.get("/{event_id}")
def get_event(event_id: str, db: Session = Depends(get_db)):
    event = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
        joinedload(Event.sources),
        joinedload(Event.perspectives),
        joinedload(Event.media),
    ).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return {
        "id": event.id,
        "date": event.date.isoformat(),
        "date_end": event.date_end.isoformat() if event.date_end else None,
        "date_precision": event.date_precision,
        "category": event.category,
        "tags": event.tags or [],
        "importance": event.importance,
        "created_at": event.created_at.isoformat(),
        "updated_at": event.updated_at.isoformat(),
        "titles": [
            {"id": t.id, "event_id": t.event_id, "language": t.language, "title": t.title}
            for t in event.titles
        ],
        "descriptions": [
            {"id": d.id, "event_id": d.event_id, "language": d.language, "summary": d.summary, "content": d.content}
            for d in event.descriptions
        ],
        "location": (
            {
                "id": event.location.id,
                "event_id": event.location.event_id,
                "lat": event.location.lat,
                "lng": event.location.lng,
                "country": event.location.country,
                "names": event.location.names or {},
            }
            if event.location
            else None
        ),
        "sources": [
            {"id": s.id, "event_id": s.event_id, "language": s.language, "url": s.url, "title": s.title, "publisher": s.publisher, "reliability": s.reliability}
            for s in event.sources
        ],
        "perspectives": [
            {"id": p.id, "event_id": p.event_id, "country_code": p.country_code, "language": p.language, "viewpoint": p.viewpoint, "source_url": p.source_url}
            for p in event.perspectives
        ],
        "media": [
            {"id": m.id, "event_id": m.event_id, "media_type": m.media_type, "url": m.url, "caption": m.caption or {}, "credit": m.credit}
            for m in event.media
        ],
    }


@router.post("", status_code=201)
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    event = Event(
        date=data.date,
        date_end=data.date_end,
        date_precision=data.date_precision,
        category=data.category,
        tags=data.tags,
        importance=data.importance,
    )
    db.add(event)
    db.flush()

    for t in data.titles:
        db.add(EventTitle(event_id=event.id, language=t.language, title=t.title))
    for d in data.descriptions:
        db.add(EventDescription(event_id=event.id, language=d.language, summary=d.summary, content=d.content))
    if data.location:
        loc = data.location
        db.add(EventLocation(event_id=event.id, lat=loc.lat, lng=loc.lng, country=loc.country, names=loc.names))

    db.commit()
    return {"id": event.id}


@router.put("/{event_id}")
def update_event(event_id: str, data: EventUpdate, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(event, key, value)

    db.commit()
    return {"status": "updated"}


@router.delete("/{event_id}")
def delete_event(event_id: str, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(event)
    db.commit()
    return {"status": "deleted"}
