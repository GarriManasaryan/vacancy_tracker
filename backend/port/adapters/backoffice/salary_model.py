from typing import Optional

from pydantic import BaseModel


class SalaryCreationRequest(BaseModel):
    min: Optional[int] = None
    max: Optional[int] = None


class SalaryBackofficeModel(BaseModel):
    id: str
    min: Optional[int]
    max: Optional[int]
