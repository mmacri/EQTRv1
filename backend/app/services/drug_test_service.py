from . import CRUDBase
from ..models.drug_test import DrugTest
from ..schemas.drug_test import DrugTestCreate, DrugTestUpdate

class DrugTestService(CRUDBase[DrugTest, DrugTestCreate]):
    pass

drug_test_service = DrugTestService(DrugTest)
