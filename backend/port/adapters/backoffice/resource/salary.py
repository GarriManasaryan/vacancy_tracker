from fastapi import Depends

from application.salary_service import SalaryService
from config.dependencies import validate_salary_creation_request
from domain.repo.salary_repo import SalaryRepo
from port.adapters.backoffice.salary_model import (
    SalaryBackofficeModel,
    SalaryCreationRequest,
)


class SalaryController:
    def __init__(self, repository: SalaryRepo):
        self._service = SalaryService(repository=repository)

    def all(self) -> list[SalaryBackofficeModel]:
        return self._service.all()

    def save(
        self,
        creation_request: SalaryCreationRequest = Depends(
            validate_salary_creation_request
        ),
    ):
        return self._service.save(creation_request=creation_request)
