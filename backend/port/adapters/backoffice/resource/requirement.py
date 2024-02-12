from dependency_injector.wiring import inject
from fastapi import APIRouter

from application.requirement_service import RequirementService
from port.adapters.backoffice.projections.requirement_proj import (
    RequirementsProjection,
)
from port.adapters.backoffice.requirement_model import (
    RequirementsCreationRequest,
    RequirementsBackofficeModel,
)
from port.adapters.persistence.postgresql_requirements_repo import (
    PostgreSQLRequirementsProjection,
)

# _service = RequirementsService(
#     repository=PostgreSQLRequirementsProjection()
# )
#
# requirements_router = APIRouter(prefix="/requirements", tags=["requirements"])
#
#
# @requirements_router.get("")
# def all_requirements() -> list[RequirementsBackofficeModel]:
#     return _service.all()
#
#
# @requirements_router.post("")
# def save_requirements(requirements_creation_request: RequirementsCreationRequest) -> None:
#     return _service.save(requirements_creation_request=requirements_creation_request)


class RequirementsController:
    @inject
    def __init__(self):
        self._service = RequirementService(
            repository=PostgreSQLRequirementsProjection()
        )

    def all(self) -> list[RequirementsBackofficeModel]:
        return self._service.all()

    def save(
        self, requirements_creation_request: RequirementsCreationRequest
    ):
        return self._service.save(
            requirements_creation_request=requirements_creation_request
        )
