from typing import Protocol

from config.app import DbConnector
from domain.salary import Salary


class SalaryRepo(Protocol):

    def save(self, salary: Salary) -> None: ...

    def all(self) -> list[Salary]: ...
