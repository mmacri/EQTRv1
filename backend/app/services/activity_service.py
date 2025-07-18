from . import CRUDBase
from ..models.activity import Activity
from ..schemas.activity import ActivityCreate, ActivityUpdate

class ActivityService(CRUDBase[Activity, ActivityCreate]):
    pass

activity_service = ActivityService(Activity)
