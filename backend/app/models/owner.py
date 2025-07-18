import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from ..db.base import Base

class Owner(Base):
    __tablename__ = "owners"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    contact_info = Column(String)

    horses = relationship("Horse", back_populates="owner")
