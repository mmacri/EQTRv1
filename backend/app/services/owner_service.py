from . import CRUDBase
from ..models.owner import Owner
from ..schemas.owner import OwnerCreate, OwnerUpdate

class OwnerService(CRUDBase[Owner, OwnerCreate]):
    pass

owner_service = OwnerService(Owner)
