import uuid
from datetime import date, datetime

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text, Date, DateTime, JSON
from sqlalchemy.orm import relationship

from .database import Base


def generate_uuid():
    return str(uuid.uuid4())


class Event(Base):
    __tablename__ = "events"

    id = Column(String, primary_key=True, default=generate_uuid)
    date = Column(Date, nullable=False, index=True)
    date_end = Column(Date, nullable=True)
    date_precision = Column(String, default="day")  # year, month, day
    category = Column(String, index=True)
    tags = Column(JSON, default=list)
    importance = Column(Integer, default=0)  # 0-100 significance score
    wiki_qid = Column(String, nullable=True, index=True)  # WikiData Q-id for cross-linking
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Multilingual content
    titles = relationship("EventTitle", back_populates="event", cascade="all, delete-orphan")
    descriptions = relationship("EventDescription", back_populates="event", cascade="all, delete-orphan")
    location = relationship("EventLocation", back_populates="event", uselist=False, cascade="all, delete-orphan")
    sources = relationship("EventSource", back_populates="event", cascade="all, delete-orphan")
    perspectives = relationship("EventPerspective", back_populates="event", cascade="all, delete-orphan")
    media = relationship("EventMedia", back_populates="event", cascade="all, delete-orphan")


class EventTitle(Base):
    __tablename__ = "event_titles"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    language = Column(String(10), nullable=False, index=True)  # zh_tw, en, ja, ko
    title = Column(Text, nullable=False)

    event = relationship("Event", back_populates="titles")


class EventDescription(Base):
    __tablename__ = "event_descriptions"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    language = Column(String(10), nullable=False, index=True)
    summary = Column(Text, nullable=True)
    content = Column(Text, nullable=True)

    event = relationship("Event", back_populates="descriptions")


class EventLocation(Base):
    __tablename__ = "event_locations"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False, unique=True)
    lat = Column(Float, nullable=True)
    lng = Column(Float, nullable=True)
    country = Column(String(10), nullable=True)
    names = Column(JSON, default=dict)  # {"zh_tw": "北京", "en": "Beijing", ...}

    event = relationship("Event", back_populates="location")


class EventSource(Base):
    __tablename__ = "event_sources"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    language = Column(String(10), nullable=False)
    url = Column(Text, nullable=False)
    title = Column(Text, nullable=True)
    publisher = Column(String, nullable=True)
    reliability = Column(Float, default=0.7)

    event = relationship("Event", back_populates="sources")


class EventPerspective(Base):
    __tablename__ = "event_perspectives"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    country_code = Column(String(10), nullable=False, index=True)  # TW, JP, KR, US, GB, CN
    language = Column(String(10), nullable=False)
    viewpoint = Column(Text, nullable=False)
    source_url = Column(Text, nullable=True)

    event = relationship("Event", back_populates="perspectives")


class EventMedia(Base):
    __tablename__ = "event_media"

    id = Column(String, primary_key=True, default=generate_uuid)
    event_id = Column(String, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    media_type = Column(String(20))  # photo, video, audio
    url = Column(Text, nullable=False)
    caption = Column(JSON, default=dict)
    credit = Column(String, nullable=True)

    event = relationship("Event", back_populates="media")
