import uuid
from sqlalchemy import Column, String, Integer, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.base import Base

class ActivityTypeEnum(str, Enum):
    TRAINING = "training"
    RACING = "racing"
    WALKING = "walking"
    STABLED = "stabled"

class Activity(Base):
    __tablename__ = "activities"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    horse_id = Column(String, ForeignKey("horses.id"))
    activity_type = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    location = Column(String)
    location_id = Column(String, ForeignKey("locations.id"))
    notes = Column(String)

    location_rel = relationship(
        "Location", back_populates="activities", foreign_keys=[location_id]
    )
    horse = relationship("Horse", back_populates="activities")
