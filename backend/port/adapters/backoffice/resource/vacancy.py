from fastapi import Depends

from application.vacancy_service import VacancyService
from config.dependencies import (
    validate_vacancy_creation_request,
)
from domain.repo.vacancy_repo import VacancyRepo
from port.adapters.backoffice.vacancy_model import (
    VacancyBackofficeModel,
    VacancyCreationRequest,
)


class VacancyController:
    def __init__(self, repository: VacancyRepo):
        self._service = VacancyService(repo=repository)

    def all(self) -> list[VacancyBackofficeModel]:
        return self._service.all()

    def save(
        self,
        creation_request: VacancyCreationRequest,
    ):
        return self._service.save(creation_request=creation_request)
