from datetime import datetime

from common.decorators import transactional
from domain.id_generator import IdGenerator
from domain.location import Location
from domain.repo.location_repo import LocationRepo
from domain.repo.vacancy_repo import VacancyRepo
from domain.vacancy import Vacancy
from port.adapters.backoffice.location_model import (
    LocationCreationRequest,
    LocationBackofficeModel,
)
from port.adapters.backoffice.vacancy_model import (
    VacancyCreationRequest,
    VacancyBackofficeModel,
)


class VacancyService:
    def __init__(self, repo: VacancyRepo):
        self.repo = repo

    @transactional
    def save(self, creation_request: VacancyCreationRequest) -> None:
        self.repo.save(
            vacancy=Vacancy(
                id=IdGenerator.generate(module_prefix="vcn"),
                title=creation_request.title,
                description=creation_request.description,
                company_id=creation_request.company_id,
                salary_id=creation_request.salary_id,
                location_id=creation_request.location_id,
                url=creation_request.url,
                submitted_at=datetime.strptime(creation_request.submitted_at, '%Y-%m-%dT%H:%M:%S.%f%z'),
            )
        )

    @transactional
    def all(self) -> list[VacancyBackofficeModel]:
        return [
            VacancyBackofficeModel(
                id=i.id,
                title=i.title,
                description=i.description,
                company_id=i.company_id,
                salary_id=i.salary_id,
                location_id=i.location_id,
                url=i.url,
                submitted_at=i.submitted_at,
            )
            for i in self.repo.all()
        ]
