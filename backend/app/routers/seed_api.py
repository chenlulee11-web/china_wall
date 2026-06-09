import sys
from datetime import date
from pathlib import Path

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from crawler.seed import SEED_EVENTS
from ..database import get_db
from ..models import Event, EventTitle, EventDescription, EventLocation, EventSource, EventPerspective

router = APIRouter(prefix="/api/seed", tags=["seed"])


@router.post("")
def seed_database(db: Session = Depends(get_db)):
    existing = db.query(Event).count()
    if existing > 0:
        return {"status": "skipped", "message": f"Database already has {existing} events"}

    count = 0
    for ev_data in SEED_EVENTS:
        ev = Event(
            date=ev_data["date"] if isinstance(ev_data["date"], date) else date.fromisoformat(ev_data["date"]),
            date_end=date.fromisoformat(ev_data["date_end"]) if ev_data.get("date_end") else None,
            date_precision=ev_data.get("date_precision", "day"),
            category=ev_data.get("category"),
            tags=ev_data.get("tags", []),
            importance=ev_data.get("importance", 0),
        )
        db.add(ev)
        db.flush()

        for lang, title in ev_data.get("titles", {}).items():
            db.add(EventTitle(event_id=ev.id, language=lang, title=title))
        for lang, desc in ev_data.get("descriptions", {}).items():
            db.add(EventDescription(event_id=ev.id, language=lang, summary=desc[:500] if desc else None, content=desc))

        loc = ev_data.get("location")
        if loc:
            db.add(EventLocation(event_id=ev.id, lat=loc.get("lat"), lng=loc.get("lng"), country=loc.get("country"), names=loc.get("names", {})))

        for src in ev_data.get("sources", []):
            db.add(EventSource(event_id=ev.id, language=src.get("lang", "en"), url=src["url"], publisher=src.get("publisher"), reliability=src.get("reliability", 0.7)))

        for persp in ev_data.get("perspectives", []):
            db.add(EventPerspective(event_id=ev.id, country_code=persp.get("country", ""), language=persp.get("lang", "en"), viewpoint=persp.get("viewpoint", "")))

        count += 1

    db.commit()
    return {"status": "success", "events_imported": count}
