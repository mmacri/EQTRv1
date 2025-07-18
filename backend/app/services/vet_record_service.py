from . import CRUDBase
from ..models.vet_record import VetRecord
from ..schemas.vet_record import VetRecordCreate, VetRecordUpdate

class VetRecordService(CRUDBase[VetRecord, VetRecordCreate]):
    pass

vet_record_service = VetRecordService(VetRecord)
