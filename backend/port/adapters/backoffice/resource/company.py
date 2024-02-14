from application.company_service import CompanyService
from domain.repo.company_repo import CompanyRepo
from port.adapters.backoffice.company_model import (
    CompanyBackofficeModel,
    CompanyCreationRequest,
)


class CompanyController:
    def __init__(self, repository: CompanyRepo):
        self._service = CompanyService(repository=repository)

    def all(self) -> list[CompanyBackofficeModel]:
        return self._service.all()

    def save(self, creation_request: CompanyCreationRequest):
        return self._service.save(creation_request=creation_request)
