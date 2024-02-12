from dependency_injector.wiring import inject

from config.app import DbConnector
from domain.requirement import Requirement
from port.adapters.backoffice.projections.requirement_proj import RequirementsProjection
from port.adapters.persistence.model.requirement_sql_model import RequirementSQLModel
from port.adapters.persistence.postgresql_executer import select, update


class PostgreSQLRequirementsProjection(RequirementsProjection):
    @inject
    def __init__(self):
        pass

    def save(self, requirements: Requirement, db_cursor: DbConnector = None) -> None:
        sql_template = (
            f"insert into {RequirementSQLModel.table}"
            f"({RequirementSQLModel.id_col}, {RequirementSQLModel.name_col}) "
            f"values"
            f"('{requirements.id}', '{requirements.name}')"
        )
        update(cursor=db_cursor, sql_template=sql_template)

    def all(self, db_cursor: DbConnector = None) -> list[Requirement]:
        sql_template = f"select * from {RequirementSQLModel.table}"
        return [Requirement(**i) for i in select(cursor=db_cursor, sql_template=sql_template)]
