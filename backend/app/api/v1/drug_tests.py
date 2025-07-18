from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import DrugTest, DrugTestCreate, DrugTestUpdate
from ...services.drug_test_service import drug_test_service
from ...db import SessionLocal

router = APIRouter(prefix="/drug-tests", tags=["drug_tests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DrugTest)
def create_drug_test(drug_test_in: DrugTestCreate, db: Session = Depends(get_db)):
    return drug_test_service.create(db, drug_test_in)

@router.get("/{drug_test_id}", response_model=DrugTest)
def read_drug_test(drug_test_id: str, db: Session = Depends(get_db)):
    drug_test = drug_test_service.get(db, drug_test_id)
    if not drug_test:
        raise HTTPException(status_code=404, detail="Drug test not found")
    return drug_test

@router.put("/{drug_test_id}", response_model=DrugTest)
def update_drug_test(drug_test_id: str, drug_test_in: DrugTestUpdate, db: Session = Depends(get_db)):
    drug_test = drug_test_service.get(db, drug_test_id)
    if not drug_test:
        raise HTTPException(status_code=404, detail="Drug test not found")
    return drug_test_service.update(db, drug_test, drug_test_in)

@router.delete("/{drug_test_id}", response_model=DrugTest)
def delete_drug_test(drug_test_id: str, db: Session = Depends(get_db)):
    drug_test = drug_test_service.get(db, drug_test_id)
    if not drug_test:
        raise HTTPException(status_code=404, detail="Drug test not found")
    return drug_test_service.remove(db, drug_test_id)

@router.get("/", response_model=list[DrugTest])
def list_drug_tests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return drug_test_service.get_multi(db, skip=skip, limit=limit)
