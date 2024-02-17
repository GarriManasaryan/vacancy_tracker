from dependency_injector.wiring import inject

from domain.repo.requirement_repo import RequirementsRepo
from domain.requirement import Requirement
from port.adapters.persistence.model.requirement_sql_model import RequirementSQLModel
from port.adapters.persistence.postgresql_executer import select, update, get_cursor


class PostgreSQLRequirementsRepo(RequirementsRepo):
    def save(self, requirements: Requirement) -> None:
        cursor = get_cursor()
        sql_template = (
            f"insert into {RequirementSQLModel.table}"
            f"({RequirementSQLModel.id_col}, {RequirementSQLModel.name_col}) "
            f"values"
            f"('{requirements.id}', '{requirements.name}')"
        )
        update(cursor=cursor, sql_template=sql_template)

    def all(self) -> list[Requirement]:
        cursor = get_cursor()
        sql_template = f"select * from {RequirementSQLModel.table}"
        return [
            Requirement(**i) for i in select(cursor=cursor, sql_template=sql_template)
        ]
