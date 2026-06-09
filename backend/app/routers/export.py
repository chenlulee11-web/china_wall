import csv
import io
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, joinedload

from ..database import get_db
from ..models import Event, EventTitle, EventDescription, EventLocation, EventSource, EventPerspective

router = APIRouter(prefix="/api/export", tags=["export"])


def _get_title(event: Event, lang: str = "en") -> str:
    match = [t for t in event.titles if t.language == lang]
    return match[0].title if match else (event.titles[0].title if event.titles else "")


def _get_description(event: Event, lang: str = "en") -> str:
    match = [d for d in event.descriptions if d.language == lang]
    if match:
        return match[0].content or match[0].summary or ""
    return ""


def _get_location_name(event: Event) -> str:
    if event.location:
        names = event.location.names or {}
        return names.get("en") or names.get("zh_tw") or event.location.country or ""
    return ""


@router.get("/events/csv")
def export_events_csv(
    lang: str = Query("en"),
    category: Optional[str] = Query(None),
    q: Optional[str] = Query(None),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
        joinedload(Event.sources),
        joinedload(Event.perspectives),
    )

    if category:
        query = query.filter(Event.category == category)
    if date_from:
        query = query.filter(Event.date >= date_from)
    if date_to:
        query = query.filter(Event.date <= date_to)
    if q:
        term = f"%{q}%"
        query = query.join(EventTitle).filter(EventTitle.title.ilike(term)).distinct()

    events = query.order_by(Event.date.asc()).all()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "ID", "Date", "Date End", "Precision", "Category",
        "Tags", "Importance", "Title", "Description",
        "Location", "Source Count", "Perspective Count",
    ])

    for e in events:
        writer.writerow([
            e.id,
            e.date.isoformat(),
            e.date_end.isoformat() if e.date_end else "",
            e.date_precision,
            e.category or "",
            ", ".join(e.tags or []),
            e.importance,
            _get_title(e, lang),
            _get_description(e, lang),
            _get_location_name(e),
            len(e.sources),
            len(e.perspectives),
        ])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=events_{date.today().isoformat()}.csv"},
    )


@router.get("/events/{event_id}/csv")
def export_event_csv(event_id: str, lang: str = Query("en"), db: Session = Depends(get_db)):
    event = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
        joinedload(Event.sources),
        joinedload(Event.perspectives),
    ).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Field", "Value"])
    writer.writerow(["ID", event.id])
    writer.writerow(["Date", event.date.isoformat()])
    writer.writerow(["Date End", event.date_end.isoformat() if event.date_end else ""])
    writer.writerow(["Precision", event.date_precision])
    writer.writerow(["Category", event.category or ""])
    writer.writerow(["Tags", ", ".join(event.tags or [])])
    writer.writerow(["Importance", event.importance])
    writer.writerow(["Title", _get_title(event, lang)])
    writer.writerow(["Description", _get_description(event, lang)])
    writer.writerow(["Location", _get_location_name(event)])

    for i, s in enumerate(event.sources, 1):
        writer.writerow([f"Source {i} URL", s.url])
        writer.writerow([f"Source {i} Title", s.title or ""])
        writer.writerow([f"Source {i} Publisher", s.publisher or ""])

    for i, p in enumerate(event.perspectives, 1):
        writer.writerow([f"Perspective {i} ({p.country_code})", p.viewpoint])

    output.seek(0)
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=event_{event_id}_{date.today().isoformat()}.csv"},
    )


@router.get("/events/pdf")
def export_events_pdf(
    lang: str = Query("en"),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import (
            SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
        )
        from reportlab.lib import colors
    except ImportError:
        raise HTTPException(status_code=500, detail="PDF export requires reportlab: pip install reportlab")

    query = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
    )
    if category:
        query = query.filter(Event.category == category)
    events = query.order_by(Event.date.asc()).all()

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title2", parent=styles["Heading2"], spaceAfter=6, spaceBefore=12)
    normal = styles["Normal"]
    small = ParagraphStyle("Small", parent=normal, fontSize=9, leading=12)

    elements = []
    elements.append(Paragraph("China Wall - Historical Events Report", styles["Title"]))
    elements.append(Spacer(1, 6*mm))

    for e in events:
        t = _get_title(e, lang)
        d = _get_description(e, lang)[:500]
        loc = _get_location_name(e)
        date_str = e.date.isoformat()
        if e.date_end:
            date_str += f" ~ {e.date_end.isoformat()}"

        elements.append(Paragraph(f"{t} ({date_str})", title_style))
        if d:
            elements.append(Paragraph(d, small))
        if loc:
            elements.append(Paragraph(f"<i>Location: {loc}</i>", small))
        elements.append(Spacer(1, 3*mm))

    doc.build(elements)
    buf.seek(0)

    return StreamingResponse(
        buf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=events_{date.today().isoformat()}.pdf"},
    )


@router.get("/events/{event_id}/pdf")
def export_event_pdf(event_id: str, lang: str = Query("en"), db: Session = Depends(get_db)):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
    except ImportError:
        raise HTTPException(status_code=500, detail="PDF export requires reportlab: pip install reportlab")

    event = db.query(Event).options(
        joinedload(Event.titles),
        joinedload(Event.descriptions),
        joinedload(Event.location),
        joinedload(Event.sources),
        joinedload(Event.perspectives),
    ).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, topMargin=20*mm, bottomMargin=20*mm)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title", parent=styles["Title"], spaceAfter=12)
    heading = ParagraphStyle("Heading", parent=styles["Heading2"], spaceAfter=6, spaceBefore=12)
    normal = styles["Normal"]
    small = ParagraphStyle("Small", parent=normal, fontSize=10, leading=14)

    elements = []
    elements.append(Paragraph(_get_title(event, lang), title_style))

    date_str = event.date.isoformat()
    if event.date_end:
        date_str += f" ~ {event.date_end.isoformat()}"
    elements.append(Paragraph(f"<b>Date:</b> {date_str}  |  <b>Category:</b> {event.category or 'N/A'}  |  <b>Importance:</b> {event.importance}", small))
    elements.append(Spacer(1, 4*mm))

    desc = _get_description(event, lang)
    if desc:
        elements.append(Paragraph("Description", heading))
        elements.append(Paragraph(desc, normal))
        elements.append(Spacer(1, 3*mm))

    if event.location:
        loc_name = _get_location_name(event)
        elements.append(Paragraph(f"<b>Location:</b> {loc_name}", normal))
        if event.location.lat and event.location.lng:
            elements.append(Paragraph(f"<b>Coordinates:</b> {event.location.lat}, {event.location.lng}", small))
        elements.append(Spacer(1, 3*mm))

    if event.perspectives:
        elements.append(Paragraph("Perspectives by Country", heading))
        for p in event.perspectives:
            elements.append(Paragraph(f"<b>{p.country_code}:</b> {p.viewpoint[:300]}", small))
            elements.append(Spacer(1, 2*mm))
        elements.append(Spacer(1, 3*mm))

    if event.sources:
        elements.append(Paragraph("Sources", heading))
        for s in event.sources:
            elements.append(Paragraph(f"<a href=\"{s.url}\">{s.title or s.url}</a> <i>({s.publisher or ''}, {s.language})</i>", small))
        elements.append(Spacer(1, 3*mm))

    if event.tags:
        elements.append(Paragraph(f"<b>Tags:</b> {', '.join(event.tags)}", small))

    doc.build(elements)
    buf.seek(0)

    return StreamingResponse(
        buf,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=event_{event_id}_{date.today().isoformat()}.pdf"},
    )
