from pydantic import BaseModel
from typing import Optional
from datetime import date

class VetRecordBase(BaseModel):
    horse_id: str
    visit_date: Optional[date] = None
    notes: Optional[str] = None
    injury_type: Optional[str] = None
    treatment: Optional[str] = None
    follow_up: Optional[str] = None

class VetRecordCreate(VetRecordBase):
    pass

class VetRecordUpdate(VetRecordBase):
    pass

class VetRecordInDBBase(VetRecordBase):
    id: str

    class Config:
        orm_mode = True

class VetRecord(VetRecordInDBBase):
    pass
