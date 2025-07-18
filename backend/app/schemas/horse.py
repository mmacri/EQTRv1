from pydantic import BaseModel
from typing import Optional

class HorseBase(BaseModel):
    name: str
    owner_id: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    notes: Optional[str] = None

class HorseCreate(HorseBase):
    pass

class HorseUpdate(HorseBase):
    pass

class HorseInDBBase(HorseBase):
    id: str

    class Config:
        orm_mode = True

class Horse(HorseInDBBase):
    pass
