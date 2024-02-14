from application.requirement_service import RequirementService
from domain.repo.requirement_repo import RequirementsRepo
from port.adapters.backoffice.requirement_model import (
    RequirementsCreationRequest,
    RequirementsBackofficeModel,
)
from port.adapters.persistence.postgresql_requirements_repo import (
    PostgreSQLRequirementsRepo,
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
    def __init__(self, repository: RequirementsRepo):
        self._service = RequirementService(
            repository=repository
        )

    def all(self) -> list[RequirementsBackofficeModel]:
        return self._service.all()

    def save(self, requirements_creation_request: RequirementsCreationRequest):
        return self._service.save(
            creation_request=requirements_creation_request
        )
