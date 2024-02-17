from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Vacancy(BaseModel):
    id: str
    title: str
    description: str
    company_id: str
    url: str
    salary_id: Optional[str] = None
    location_id: Optional[str] = None
    submitted_at: Optional[datetime] = None
