from fastapi import HTTPException

from config.app import ConnectionFromPool
from domain.id_generator import IdGenerator
from domain.salary import Salary
from port.adapters.backoffice.projections.salary_proj import SalaryProjection
from port.adapters.backoffice.salary_model import (
    SalaryCreationRequest,
    SalaryBackofficeModel,
)


class SalaryService:

    def __init__(self, repository: SalaryProjection):
        self.repository = repository

    def save(self, creation_request: SalaryCreationRequest) -> None:
        with ConnectionFromPool() as cursor:
            if creation_request.min is None and creation_request.max is None:
                raise HTTPException(
                    status_code=404, detail="Both min and max values cant be empty"
                )
            self.repository.save(
                salary=Salary(
                    id=IdGenerator.generate("slr"),
                    min=creation_request.min if creation_request.min else 0,
                    max=creation_request.max if creation_request.max else 0,
                ),
                db_cursor=cursor,
            )

    def all(self) -> list[SalaryBackofficeModel]:
        with ConnectionFromPool() as cursor:
            return [
                SalaryBackofficeModel(id=i.id, min=i.min, max=i.max)
                for i in self.repository.all(db_cursor=cursor)
            ]
