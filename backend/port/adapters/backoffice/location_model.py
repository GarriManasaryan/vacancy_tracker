from typing import Optional

from pydantic import BaseModel


class LocationBackofficeModel(BaseModel):
    id: str
    country: str
    state: Optional[str]
    city: str


class LocationCreationRequest(BaseModel):
    country: str
    state: Optional[str]
    city: str
