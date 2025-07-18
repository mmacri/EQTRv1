import uuid
from sqlalchemy import Column, String, Integer, Enum
from sqlalchemy.orm import relationship
from ..db.base import Base

class LocationTypeEnum(str, Enum):
    BARN = "barn"
    TRACK = "track"
    GATE = "gate"
    WALKING_PATH = "walking_path"

class Location(Base):
    __tablename__ = "locations"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String)
    capacity = Column(Integer)
    notes = Column(String)

    activities = relationship("Activity", back_populates="location_rel")
