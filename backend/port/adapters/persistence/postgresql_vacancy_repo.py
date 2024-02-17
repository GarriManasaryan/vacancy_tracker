from domain.repo.vacancy_repo import VacancyRepo
from domain.vacancy import Vacancy
from port.adapters.persistence.model.vacancy_sql_model import VacancySQLModel
from port.adapters.persistence.postgresql_executer import (
    get_cursor,
    update,
    all_entities,
)


class PostgreSQLVacancyRepo(VacancyRepo):
    def save(self, vacancy: Vacancy) -> None:
        cursor = get_cursor()
        sql_template = (
            f"insert into {VacancySQLModel.table}"
            f"({VacancySQLModel.id}, {VacancySQLModel.title}, {VacancySQLModel.description}, "
            f"{VacancySQLModel.company_id}, {VacancySQLModel.salary_id}, {VacancySQLModel.location_id}, "
            f"{VacancySQLModel.url}, {VacancySQLModel.submitted_at}) "
            f"values "
            f"('{vacancy.id}', '{vacancy.title}', '{vacancy.description}', '{vacancy.company_id}', "
            f"'{str(vacancy.salary_id)}', '{str(vacancy.location_id)}', '{vacancy.url}', "
            f"'{str(vacancy.submitted_at)}')"
        )
        if not vacancy.salary_id:
            sql_template = sql_template.replace(
                f", '{str(vacancy.salary_id)}'", ""
            ).replace(f", {VacancySQLModel.salary_id}", "")
        if not vacancy.location_id:
            sql_template = sql_template.replace(
                f", '{str(vacancy.location_id)}'", ""
            ).replace(f", {VacancySQLModel.location_id}", "")
        if not vacancy.submitted_at:
            sql_template = sql_template.replace(
                f", '{str(vacancy.submitted_at)}'", ""
            ).replace(f", {VacancySQLModel.submitted_at}", "")
        update(cursor=cursor, sql_template=sql_template)

    def all(self) -> list[Vacancy]:
        return all_entities(table=VacancySQLModel.table, entity=Vacancy)
