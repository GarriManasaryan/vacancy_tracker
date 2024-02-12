from fastapi import APIRouter

from application.company_service import CompanyService
from application.requirement_service import RequirementService
from application.salary_service import SalaryService
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
from port.adapters.backoffice.salary_model import (
    SalaryBackofficeModel,
    SalaryCreationRequest,
)
from port.adapters.persistence.postgresql_company_repo import (
    PostgreSQLCompanyProjection,
)
from port.adapters.persistence.postgresql_requirements_repo import (
    PostgreSQLRequirementsProjection,
)
from port.adapters.persistence.postgresql_salary_repo import PostgreSQLSalaryProjection


class SalaryController:
    def __init__(self):
        self._service = SalaryService(repository=PostgreSQLSalaryProjection())

    def all(self) -> list[SalaryBackofficeModel]:
        return self._service.all()

    def save(self, creation_request: SalaryCreationRequest):
        return self._service.save(creation_request=creation_request)
