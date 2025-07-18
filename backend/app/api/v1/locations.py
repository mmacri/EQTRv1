from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Location, LocationCreate, LocationUpdate
from ...services.location_service import location_service
from ...db import SessionLocal

router = APIRouter(prefix="/locations", tags=["locations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Location)
def create_location(location_in: LocationCreate, db: Session = Depends(get_db)):
    return location_service.create(db, location_in)

@router.get("/{location_id}", response_model=Location)
def read_location(location_id: str, db: Session = Depends(get_db)):
    location = location_service.get(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.put("/{location_id}", response_model=Location)
def update_location(location_id: str, location_in: LocationUpdate, db: Session = Depends(get_db)):
    location = location_service.get(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location_service.update(db, location, location_in)

@router.delete("/{location_id}", response_model=Location)
def delete_location(location_id: str, db: Session = Depends(get_db)):
    location = location_service.get(db, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location_service.remove(db, location_id)

@router.get("/", response_model=list[Location])
def list_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return location_service.get_multi(db, skip=skip, limit=limit)
