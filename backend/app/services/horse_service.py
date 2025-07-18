from . import CRUDBase
from sqlalchemy.orm import Session
from ..models.horse import Horse
from ..schemas.horse import HorseCreate, HorseUpdate

class HorseService(CRUDBase[Horse, HorseCreate]):
    def get_by_name(self, db: Session, name: str) -> Horse | None:
        return db.query(self.model).filter(Horse.name == name).first()

    def get_by_owner(
        self, db: Session, owner_id: str | None, skip: int = 0, limit: int = 100
    ):
        q = db.query(self.model)
        if owner_id:
            q = q.filter(Horse.owner_id == owner_id)
        return q.offset(skip).limit(limit).all()

horse_service = HorseService(Horse)
