from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...schemas import Horse, HorseCreate, HorseUpdate
from ...services.horse_service import horse_service
from .realtime import broadcast
from ...deps import (
    get_db,
    require_admin,
    require_owner_or_admin,
    get_current_user,
    User,
)

router = APIRouter(prefix="/horses", tags=["horses"])

@router.post("/", response_model=Horse, dependencies=[Depends(require_admin)])
def create_horse(horse_in: HorseCreate, db: Session = Depends(get_db)):
    existing = horse_service.get_by_name(db, horse_in.name)
    if existing:
        raise HTTPException(status_code=400, detail="Horse name already exists")
    horse = horse_service.create(db, horse_in)
    import asyncio
    asyncio.create_task(broadcast("horse_update"))
    return horse

@router.get("/{horse_id}", response_model=Horse)
def read_horse(
    horse_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(require_owner_or_admin),
):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if user.role == "owner" and horse.owner_id != user.owner_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return horse

@router.put("/{horse_id}", response_model=Horse, dependencies=[Depends(require_owner_or_admin)])
def update_horse(
    horse_id: str,
    horse_in: HorseUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if user.role == "owner" and horse.owner_id != user.owner_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    horse = horse_service.update(db, horse, horse_in)
    import asyncio
    asyncio.create_task(broadcast("horse_update"))
    return horse

@router.delete("/{horse_id}", response_model=Horse, dependencies=[Depends(require_admin)])
def delete_horse(horse_id: str, db: Session = Depends(get_db)):
    horse = horse_service.get(db, horse_id)
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    result = horse_service.remove(db, horse_id)
    import asyncio
    asyncio.create_task(broadcast("horse_update"))
    return result

@router.get("/", response_model=list[Horse])
def list_horses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    user: User = Depends(require_owner_or_admin),
):
    if user.role == "owner":
        return horse_service.get_by_owner(db, user.owner_id, skip=skip, limit=limit)
    return horse_service.get_multi(db, skip=skip, limit=limit)

@router.post("/bulk_update", response_model=list[Horse], dependencies=[Depends(require_admin)])
def bulk_update_horses(horses: list[HorseUpdate], db: Session = Depends(get_db)):
    updated = []
    for h in horses:
        horse = horse_service.get(db, h.id)
        if horse:
            updated.append(horse_service.update(db, horse, h))
    return updated
