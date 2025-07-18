from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from .db.session import SessionLocal

class User:
    def __init__(self, role: str = "viewer", owner_id: str | None = None):
        self.role = role
        self.owner_id = owner_id

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(x_role: str | None = Header(default="viewer"), x_owner_id: str | None = Header(default=None)) -> User:
    return User(role=x_role, owner_id=x_owner_id)

def require_admin(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return user

def require_owner_or_admin(user: User = Depends(get_current_user)):
    if user.role not in {"admin", "owner"}:
        raise HTTPException(status_code=403, detail="Owner or admin required")
    return user
