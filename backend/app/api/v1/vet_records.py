from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import VetRecord, VetRecordCreate, VetRecordUpdate
from ...services.vet_record_service import vet_record_service
from ...db import SessionLocal

router = APIRouter(prefix="/vet-records", tags=["vet_records"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VetRecord)
def create_vet_record(vet_record_in: VetRecordCreate, db: Session = Depends(get_db)):
    return vet_record_service.create(db, vet_record_in)

@router.get("/{record_id}", response_model=VetRecord)
def read_vet_record(record_id: str, db: Session = Depends(get_db)):
    record = vet_record_service.get(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Vet record not found")
    return record

@router.put("/{record_id}", response_model=VetRecord)
def update_vet_record(record_id: str, record_in: VetRecordUpdate, db: Session = Depends(get_db)):
    record = vet_record_service.get(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Vet record not found")
    return vet_record_service.update(db, record, record_in)

@router.delete("/{record_id}", response_model=VetRecord)
def delete_vet_record(record_id: str, db: Session = Depends(get_db)):
    record = vet_record_service.get(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Vet record not found")
    return vet_record_service.remove(db, record_id)

@router.get("/", response_model=list[VetRecord])
def list_vet_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return vet_record_service.get_multi(db, skip=skip, limit=limit)
