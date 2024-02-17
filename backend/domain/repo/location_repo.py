from typing import Protocol

from domain.location import Location


class LocationRepo(Protocol):
    def save(self, location: Location) -> None: ...

    def all(self) -> list[Location]: ...
