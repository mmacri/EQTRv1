from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ActivityBase(BaseModel):
    horse_id: str
    activity_type: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    location_id: Optional[str] = None
    notes: Optional[str] = None

class ActivityCreate(ActivityBase):
    pass

class ActivityUpdate(ActivityBase):
    pass

class ActivityInDBBase(ActivityBase):
    id: str

    class Config:
        orm_mode = True

class Activity(ActivityInDBBase):
    pass
