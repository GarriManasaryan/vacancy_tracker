from dataclasses import dataclass


@dataclass
class VacancySQLModel:
    table: str = "vt_vacancies"
    id: str = "id"
    title: str = "title"
    description: str = "description"
    company_id: str = "company_id"
    salary_id: str = "salary_id"
    location_id: str = "location_id"
    url: str = "url"
    submitted_at: str = "submitted_at"
