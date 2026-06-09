from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


# --- EventTitle ---
class EventTitleBase(BaseModel):
    language: str
    title: str


class EventTitleCreate(EventTitleBase):
    pass


class EventTitleOut(EventTitleBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- EventDescription ---
class EventDescriptionBase(BaseModel):
    language: str
    summary: Optional[str] = None
    content: Optional[str] = None


class EventDescriptionCreate(EventDescriptionBase):
    pass


class EventDescriptionOut(EventDescriptionBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- EventLocation ---
class EventLocationBase(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None
    country: Optional[str] = None
    names: dict[str, str] = {}


class EventLocationCreate(EventLocationBase):
    pass


class EventLocationOut(EventLocationBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- EventSource ---
class EventSourceBase(BaseModel):
    language: str
    url: str
    title: Optional[str] = None
    publisher: Optional[str] = None
    reliability: float = 0.7


class EventSourceCreate(EventSourceBase):
    pass


class EventSourceOut(EventSourceBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- EventPerspective ---
class EventPerspectiveBase(BaseModel):
    country_code: str
    language: str
    viewpoint: str
    source_url: Optional[str] = None


class EventPerspectiveCreate(EventPerspectiveBase):
    pass


class EventPerspectiveOut(EventPerspectiveBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- EventMedia ---
class EventMediaBase(BaseModel):
    media_type: str
    url: str
    caption: dict[str, str] = {}
    credit: Optional[str] = None


class EventMediaCreate(EventMediaBase):
    pass


class EventMediaOut(EventMediaBase):
    id: str
    event_id: str

    class Config:
        from_attributes = True


# --- Event ---
class EventCreate(BaseModel):
    date: date
    date_end: Optional[date] = None
    date_precision: str = "day"
    category: Optional[str] = None
    tags: list[str] = []
    importance: int = 0
    titles: list[EventTitleCreate] = []
    descriptions: list[EventDescriptionCreate] = []
    location: Optional[EventLocationCreate] = None
    sources: list[EventSourceCreate] = []
    perspectives: list[EventPerspectiveCreate] = []
    media: list[EventMediaCreate] = []


class EventUpdate(BaseModel):
    date: Optional[date] = None
    date_end: Optional[date] = None
    date_precision: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
    importance: Optional[int] = None


class EventListItem(BaseModel):
    id: str
    date: date
    date_end: Optional[date] = None
    date_precision: str
    category: Optional[str] = None
    tags: list[str]
    importance: int
    titles: list[EventTitleOut] = []
    descriptions: list[EventDescriptionOut] = []
    location: Optional[EventLocationOut] = None
    source_count: int = 0

    class Config:
        from_attributes = True


class EventDetail(BaseModel):
    id: str
    date: date
    date_end: Optional[date] = None
    date_precision: str
    category: Optional[str] = None
    tags: list[str]
    importance: int
    created_at: datetime
    updated_at: datetime
    titles: list[EventTitleOut] = []
    descriptions: list[EventDescriptionOut] = []
    location: Optional[EventLocationOut] = None
    sources: list[EventSourceOut] = []
    perspectives: list[EventPerspectiveOut] = []
    media: list[EventMediaOut] = []

    class Config:
        from_attributes = True


# --- Search/Filter ---
class EventFilterParams(BaseModel):
    lang: Optional[str] = None
    category: Optional[str] = None
    country: Optional[str] = None
    q: Optional[str] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    importance_min: Optional[int] = None
    tags: Optional[list[str]] = None
    limit: int = 100
    offset: int = 0


class GeoFeature(BaseModel):
    event_id: str
    lat: float
    lng: float
    title: str
    date: str
    category: Optional[str] = None
    names: dict[str, str] = {}


class GeoJSONCollection(BaseModel):
    type: str = "FeatureCollection"
    features: list[dict] = []
