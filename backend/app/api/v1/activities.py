from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Activity, ActivityCreate, ActivityUpdate
from ...services.activity_service import activity_service
from ...db import SessionLocal

router = APIRouter(prefix="/activities", tags=["activities"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Activity)
def create_activity(activity_in: ActivityCreate, db: Session = Depends(get_db)):
    return activity_service.create(db, activity_in)

@router.get("/{activity_id}", response_model=Activity)
def read_activity(activity_id: str, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

@router.put("/{activity_id}", response_model=Activity)
def update_activity(activity_id: str, activity_in: ActivityUpdate, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity_service.update(db, activity, activity_in)

@router.delete("/{activity_id}", response_model=Activity)
def delete_activity(activity_id: str, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity_service.remove(db, activity_id)

@router.get("/", response_model=list[Activity])
def list_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return activity_service.get_multi(db, skip=skip, limit=limit)
