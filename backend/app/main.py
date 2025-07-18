from fastapi import FastAPI
from .db import init_db
from .api import api_v1_router

app = FastAPI(title="Delmar Horse Management")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(api_v1_router, prefix="/api/v1")
