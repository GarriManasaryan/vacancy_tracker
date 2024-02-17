from dataclasses import dataclass


@dataclass
class LocationSQLModel:
    table: str = "vt_locations"
    id: str = "id"
    country: str = "country"
    state: str = "state"
    city: str = "city"
