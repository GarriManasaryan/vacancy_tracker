from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class VacancyBackofficeModel(BaseModel):
    id: str
    title: str
    description: str
    company_id: str
    url: str
    salary_id: Optional[str] = None
    location_id: Optional[str] = None
    submitted_at: Optional[datetime] = None


class VacancyCreationRequest(BaseModel):
    title: str
    description: str
    company_id: str
    url: str
    salary_id: Optional[str] = None
    location_id: Optional[str] = None
    submitted_at: Optional[str] = None
