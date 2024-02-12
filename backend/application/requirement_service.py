from dependency_injector.wiring import inject

from config.app import ConnectionFromPool
from domain.id_generator import IdGenerator
from domain.requirement import Requirement
from port.adapters.backoffice.projections.requirement_proj import RequirementsProjection
from port.adapters.backoffice.requirement_model import RequirementsBackofficeModel, RequirementsCreationRequest


class RequirementService:
    @inject
    def __init__(self, repository: RequirementsProjection):
        self.repository = repository

    def save(self, requirements_creation_request: RequirementsCreationRequest) -> None:
        with ConnectionFromPool() as cursor:
            self.repository.save(
                requirements=Requirement(id=IdGenerator.generate("rqr"), name=requirements_creation_request.name),
                db_cursor=cursor
            )

    def all(self) -> list[RequirementsBackofficeModel]:
        with ConnectionFromPool() as cursor:
            return [RequirementsBackofficeModel(id=i.id, name=i.name) for i in self.repository.all(db_cursor=cursor)]
