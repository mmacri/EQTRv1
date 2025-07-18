from pydantic import BaseModel
from typing import Optional

class OwnerBase(BaseModel):
    name: str
    contact_info: Optional[str] = None

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(OwnerBase):
    pass

class OwnerInDBBase(OwnerBase):
    id: str

    class Config:
        orm_mode = True

class Owner(OwnerInDBBase):
    pass
