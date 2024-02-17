from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    id: str
    country: str
    city: str
    state: Optional[str] = None
