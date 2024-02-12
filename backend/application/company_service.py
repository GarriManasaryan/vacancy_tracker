from config.app import ConnectionFromPool
from domain.company import Company
from domain.id_generator import IdGenerator
from domain.requirement import Requirement
from port.adapters.backoffice.company_model import (
    CompanyCreationRequest,
    CompanyBackofficeModel,
)
from port.adapters.backoffice.projections.company_proj import CompanyProjection
from port.adapters.backoffice.projections.requirement_proj import RequirementsProjection
from port.adapters.backoffice.requirement_model import (
    RequirementsBackofficeModel,
    RequirementsCreationRequest,
)


class CompanyService:

    def __init__(self, repository: CompanyProjection):
        self.repository = repository

    def save(self, creation_request: CompanyCreationRequest) -> None:
        with ConnectionFromPool() as cursor:
            self.repository.save(
                company=Company(
                    id=IdGenerator.generate("cmp"),
                    name=creation_request.name,
                    description=creation_request.description,
                ),
                db_cursor=cursor,
            )

    def all(self) -> list[CompanyBackofficeModel]:
        with ConnectionFromPool() as cursor:
            return [
                CompanyBackofficeModel(id=i.id, name=i.name, description=i.description)
                for i in self.repository.all(db_cursor=cursor)
            ]
