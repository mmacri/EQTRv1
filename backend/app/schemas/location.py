from pydantic import BaseModel
from typing import Optional

class LocationBase(BaseModel):
    name: str
    type: Optional[str] = None
    capacity: Optional[int] = None
    notes: Optional[str] = None

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    pass

class LocationInDBBase(LocationBase):
    id: str

    class Config:
        orm_mode = True

class Location(LocationInDBBase):
    pass
