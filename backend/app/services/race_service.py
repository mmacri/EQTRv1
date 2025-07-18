from . import CRUDBase
from ..models.race import Race
from ..schemas.race import RaceCreate, RaceUpdate

class RaceService(CRUDBase[Race, RaceCreate]):
    pass

race_service = RaceService(Race)
