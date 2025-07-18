from . import CRUDBase
from ..models.horse import Horse
from ..schemas.horse import HorseCreate, HorseUpdate

class HorseService(CRUDBase[Horse, HorseCreate]):
    pass

horse_service = HorseService(Horse)
