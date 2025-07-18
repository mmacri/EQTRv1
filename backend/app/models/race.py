import uuid
from sqlalchemy import Column, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

race_horses = Table(
    "race_horses",
    Base.metadata,
    Column("race_id", String, ForeignKey("races.id")),
    Column("horse_id", String, ForeignKey("horses.id")),
)

class Race(Base):
    __tablename__ = "races"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, index=True, nullable=False)
    date = Column(Date)
    location = Column(String)
    notes = Column(String)

    horses = relationship("Horse", secondary=race_horses, back_populates="races")
    drug_tests = relationship("DrugTest", back_populates="race")
