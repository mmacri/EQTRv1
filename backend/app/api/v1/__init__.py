from fastapi import APIRouter
from . import horses, activities, locations, races, drug_tests, vet_records, owners, realtime

api_router = APIRouter()
api_router.include_router(horses.router)
api_router.include_router(activities.router)
api_router.include_router(locations.router)
api_router.include_router(races.router)
api_router.include_router(drug_tests.router)
api_router.include_router(vet_records.router)
api_router.include_router(owners.router)
api_router.include_router(realtime.router)
