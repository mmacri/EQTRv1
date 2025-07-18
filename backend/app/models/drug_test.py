import uuid
from sqlalchemy import Column, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class DrugTestResultEnum(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    PENDING = "pending"

class DrugTest(Base):
    __tablename__ = "drug_tests"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    horse_id = Column(String, ForeignKey("horses.id"))
    race_id = Column(String, ForeignKey("races.id"))
    result = Column(String, default="pending")
    date = Column(Date)
    notes = Column(String)

    horse = relationship("Horse", back_populates="drug_tests")
    race = relationship("Race", back_populates="drug_tests")
