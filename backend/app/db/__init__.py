from pathlib import Path
from .session import SessionLocal, engine, SQLALCHEMY_DATABASE_URL
from .base import Base


def init_db():
    """Initialize database and ensure database directory exists."""
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite:///"):
        db_file = SQLALCHEMY_DATABASE_URL.split("sqlite:///", 1)[1]
        Path(db_file).parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
