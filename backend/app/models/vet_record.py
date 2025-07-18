import uuid
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class VetRecord(Base):
    __tablename__ = "vet_records"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    horse_id = Column(String, ForeignKey("horses.id"))
    visit_date = Column(Date)
    notes = Column(String)
    injury_type = Column(String)
    treatment = Column(String)
    follow_up = Column(String)

    horse = relationship("Horse", back_populates="vet_records")
