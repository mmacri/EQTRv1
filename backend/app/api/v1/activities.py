from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Activity, ActivityCreate, ActivityUpdate
from ...services.activity_service import activity_service
from ...deps import get_db, require_admin

router = APIRouter(prefix="/activities", tags=["activities"])

@router.post("/", response_model=Activity, dependencies=[Depends(require_admin)])
def create_activity(activity_in: ActivityCreate, db: Session = Depends(get_db)):
    try:
        return activity_service.create(db, activity_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{activity_id}", response_model=Activity)
def read_activity(activity_id: str, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

@router.put("/{activity_id}", response_model=Activity, dependencies=[Depends(require_admin)])
def update_activity(activity_id: str, activity_in: ActivityUpdate, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    try:
        return activity_service.update(db, activity, activity_in)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{activity_id}", response_model=Activity, dependencies=[Depends(require_admin)])
def delete_activity(activity_id: str, db: Session = Depends(get_db)):
    activity = activity_service.get(db, activity_id)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity_service.remove(db, activity_id)

@router.get("/", response_model=list[Activity])
def list_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return activity_service.get_multi(db, skip=skip, limit=limit)
