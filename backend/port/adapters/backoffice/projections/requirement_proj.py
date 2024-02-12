from typing import Protocol

from config.app import DbConnector
from domain.requirement import Requirement


class RequirementsProjection(Protocol):

    def save(
        self, requirements: Requirement, db_cursor: DbConnector = None
    ) -> None: ...

    def all(self, db_cursor: DbConnector = None) -> list[Requirement]: ...
