from . import CRUDBase
from sqlalchemy.orm import Session
from ..models.activity import Activity
from ..schemas.activity import ActivityCreate, ActivityUpdate

class ActivityService(CRUDBase[Activity, ActivityCreate]):
    def create(self, db: Session, obj_in: ActivityCreate) -> Activity:
        overlap = (
            db.query(Activity)
            .filter(Activity.horse_id == obj_in.horse_id)
            .filter(Activity.end_time > obj_in.start_time)
            .filter(Activity.start_time < obj_in.end_time)
            .first()
        )
        if overlap:
            raise ValueError("Overlapping activity")
        return super().create(db, obj_in)

    def update(self, db: Session, db_obj: Activity, obj_in: ActivityUpdate) -> Activity:
        overlap = (
            db.query(Activity)
            .filter(Activity.horse_id == db_obj.horse_id)
            .filter(Activity.id != db_obj.id)
            .filter(Activity.end_time > obj_in.start_time)
            .filter(Activity.start_time < obj_in.end_time)
            .first()
        )
        if overlap:
            raise ValueError("Overlapping activity")
        return super().update(db, db_obj, obj_in)

activity_service = ActivityService(Activity)
