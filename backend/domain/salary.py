from typing import Optional

from pydantic import BaseModel


class Salary(BaseModel):
    id: str
    min: Optional[int]
    max: Optional[int]
