from . import CRUDBase
from ..models.location import Location
from ..schemas.location import LocationCreate, LocationUpdate

class LocationService(CRUDBase[Location, LocationCreate]):
    pass

location_service = LocationService(Location)
