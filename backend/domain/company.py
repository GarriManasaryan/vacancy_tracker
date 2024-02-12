from typing import Optional

from pydantic import BaseModel


class Company(BaseModel):
    id: str
    name: str
    description: Optional[str]
