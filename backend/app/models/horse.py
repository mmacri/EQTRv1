import uuid
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ..db.base import Base

class HorseStatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    RETIRED = "retired"

class Horse(Base):
    __tablename__ = "horses"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, index=True, nullable=False)
    owner_id = Column(String, ForeignKey("owners.id"), nullable=True)
    status = Column(String, default="active")
    location = Column(String, nullable=True)
    breed = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    owner = relationship("Owner", back_populates="horses")
    activities = relationship("Activity", back_populates="horse")
    drug_tests = relationship("DrugTest", back_populates="horse")
    vet_records = relationship("VetRecord", back_populates="horse")
    races = relationship("Race", secondary="race_horses", back_populates="horses")
