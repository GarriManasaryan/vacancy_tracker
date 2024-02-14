from common.decorators import transactional
from domain.id_generator import IdGenerator
from domain.repo.requirement_repo import RequirementsRepo
from domain.requirement import Requirement
from port.adapters.backoffice.requirement_model import (
    RequirementsBackofficeModel,
    RequirementsCreationRequest,
)


class RequirementService:
    def __init__(self, repository: RequirementsRepo):
        self.repository = repository

    @transactional
    def save(self, creation_request: RequirementsCreationRequest) -> None:
        self.repository.save(
            requirements=Requirement(
                id=IdGenerator.generate("rqr"), name=creation_request.name
            )
        )

    @transactional
    def all(self) -> list[RequirementsBackofficeModel]:
        return [
            RequirementsBackofficeModel(id=i.id, name=i.name)
            for i in self.repository.all()
        ]
