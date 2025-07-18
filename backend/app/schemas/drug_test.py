from pydantic import BaseModel
from typing import Optional
from datetime import date

class DrugTestBase(BaseModel):
    horse_id: str
    race_id: Optional[str] = None
    result: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None

class DrugTestCreate(DrugTestBase):
    pass

class DrugTestUpdate(DrugTestBase):
    pass

class DrugTestInDBBase(DrugTestBase):
    id: str

    class Config:
        orm_mode = True

class DrugTest(DrugTestInDBBase):
    pass
