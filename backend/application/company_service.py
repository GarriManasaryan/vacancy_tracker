from common.decorators import transactional
from domain.company import Company
from domain.repo.company_repo import CompanyRepo
from domain.id_generator import IdGenerator
from port.adapters.backoffice.company_model import (
    CompanyCreationRequest,
    CompanyBackofficeModel,
)


class CompanyService:
    def __init__(self, repository: CompanyRepo):
        self.repository = repository

    @transactional
    def save(self, creation_request: CompanyCreationRequest) -> None:
        self.repository.save(
            company=Company(
                id=IdGenerator.generate("cmp"),
                name=creation_request.name,
                description=creation_request.description,
            )
        )

    @transactional
    def all(self) -> list[CompanyBackofficeModel]:
        return [
            CompanyBackofficeModel(id=i.id, name=i.name, description=i.description)
            for i in self.repository.all()
        ]
