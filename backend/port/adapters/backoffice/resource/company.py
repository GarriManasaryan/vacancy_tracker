from fastapi import APIRouter

from application.company_service import CompanyService
from application.requirement_service import RequirementService
from port.adapters.backoffice.company_model import (
    CompanyBackofficeModel,
    CompanyCreationRequest,
)
from port.adapters.backoffice.projections.requirement_proj import (
    RequirementsProjection,
)
from port.adapters.backoffice.requirement_model import (
    RequirementsCreationRequest,
    RequirementsBackofficeModel,
)
from port.adapters.persistence.postgresql_company_repo import (
    PostgreSQLCompanyProjection,
)
from port.adapters.persistence.postgresql_requirements_repo import (
    PostgreSQLRequirementsProjection,
)


class CompanyController:
    def __init__(self):
        self._service = CompanyService(repository=PostgreSQLCompanyProjection())

    def all(self) -> list[CompanyBackofficeModel]:
        return self._service.all()

    def save(self, creation_request: CompanyCreationRequest):
        return self._service.save(
            creation_request=creation_request
        )
