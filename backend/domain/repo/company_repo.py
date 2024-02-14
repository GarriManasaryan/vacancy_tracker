from typing import Protocol

from config.app import DbConnector
from domain.company import Company


class CompanyRepo(Protocol):

    def save(self, company: Company) -> None: ...

    def all(self) -> list[Company]: ...
