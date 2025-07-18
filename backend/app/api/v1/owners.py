from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Owner, OwnerCreate, OwnerUpdate
from ...services.owner_service import owner_service
from ...db import SessionLocal

router = APIRouter(prefix="/owners", tags=["owners"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Owner)
def create_owner(owner_in: OwnerCreate, db: Session = Depends(get_db)):
    return owner_service.create(db, owner_in)

@router.get("/{owner_id}", response_model=Owner)
def read_owner(owner_id: str, db: Session = Depends(get_db)):
    owner = owner_service.get(db, owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner

@router.put("/{owner_id}", response_model=Owner)
def update_owner(owner_id: str, owner_in: OwnerUpdate, db: Session = Depends(get_db)):
    owner = owner_service.get(db, owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner_service.update(db, owner, owner_in)

@router.delete("/{owner_id}", response_model=Owner)
def delete_owner(owner_id: str, db: Session = Depends(get_db)):
    owner = owner_service.get(db, owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    return owner_service.remove(db, owner_id)

@router.get("/", response_model=list[Owner])
def list_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return owner_service.get_multi(db, skip=skip, limit=limit)
