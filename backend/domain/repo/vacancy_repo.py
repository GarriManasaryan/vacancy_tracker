from typing import Protocol

from domain.vacancy import Vacancy


class VacancyRepo(Protocol):
    def save(self, vacancy: Vacancy) -> None: ...

    def all(self) -> list[Vacancy]: ...
