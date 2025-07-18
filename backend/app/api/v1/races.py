from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Race, RaceCreate, RaceUpdate
from ...services.race_service import race_service
from ...db import SessionLocal

router = APIRouter(prefix="/races", tags=["races"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Race)
def create_race(race_in: RaceCreate, db: Session = Depends(get_db)):
    return race_service.create(db, race_in)

@router.get("/{race_id}", response_model=Race)
def read_race(race_id: str, db: Session = Depends(get_db)):
    race = race_service.get(db, race_id)
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race

@router.put("/{race_id}", response_model=Race)
def update_race(race_id: str, race_in: RaceUpdate, db: Session = Depends(get_db)):
    race = race_service.get(db, race_id)
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race_service.update(db, race, race_in)

@router.delete("/{race_id}", response_model=Race)
def delete_race(race_id: str, db: Session = Depends(get_db)):
    race = race_service.get(db, race_id)
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race_service.remove(db, race_id)

@router.get("/", response_model=list[Race])
def list_races(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return race_service.get_multi(db, skip=skip, limit=limit)
