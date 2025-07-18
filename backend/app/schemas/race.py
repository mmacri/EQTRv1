from pydantic import BaseModel
from typing import Optional
from datetime import date

class RaceBase(BaseModel):
    name: str
    date: Optional[date] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class RaceCreate(RaceBase):
    pass

class RaceUpdate(RaceBase):
    pass

class RaceInDBBase(RaceBase):
    id: str

    class Config:
        orm_mode = True

class Race(RaceInDBBase):
    pass
