from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Horse, HorseCreate, HorseUpdate
from ...services.horse_service import horse_service
from ...db import SessionLocal

router = APIRouter(prefix="/horses", tags=["horses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Horse)
def create_horse(horse_in: HorseCreate, db: Session = Depends(get_db)):
    return horse_service.create(db, horse_in)

@router.get("/{horse_id}", response_model=Horse)
def read_horse(horse_id: str, db: Session = Depends(get_db)):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    return horse

@router.put("/{horse_id}", response_model=Horse)
def update_horse(horse_id: str, horse_in: HorseUpdate, db: Session = Depends(get_db)):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    return horse_service.update(db, horse, horse_in)

@router.delete("/{horse_id}", response_model=Horse)
def delete_horse(horse_id: str, db: Session = Depends(get_db)):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    return horse_service.remove(db, horse_id)

@router.get("/", response_model=list[Horse])
def list_horses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return horse_service.get_multi(db, skip=skip, limit=limit)
