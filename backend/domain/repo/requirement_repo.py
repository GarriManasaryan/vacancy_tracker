from typing import Protocol

from domain.requirement import Requirement


class RequirementsRepo(Protocol):

    def save(self, requirements: Requirement) -> None: ...

    def all(self) -> list[Requirement]: ...
