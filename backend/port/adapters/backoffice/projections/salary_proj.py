from typing import Protocol

from config.app import DbConnector
from domain.salary import Salary


class SalaryProjection(Protocol):

    def save(self, salary: Salary, db_cursor: DbConnector = None) -> None: ...

    def all(self, db_cursor: DbConnector = None) -> list[Salary]: ...
