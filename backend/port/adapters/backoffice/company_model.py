from typing import Optional

from pydantic import BaseModel


class CompanyCreationRequest(BaseModel):
    name: str
    description: Optional[str]


class CompanyBackofficeModel(BaseModel):
    id: str
    name: str
    description: Optional[str]
