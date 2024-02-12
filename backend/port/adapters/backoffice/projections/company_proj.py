from typing import Protocol

from config.app import DbConnector
from domain.company import Company


class CompanyProjection(Protocol):

    def save(self, company: Company, db_cursor: DbConnector = None) -> None: ...

    def all(self, db_cursor: DbConnector = None) -> list[Company]: ...
