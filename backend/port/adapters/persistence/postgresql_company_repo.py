from config.app import DbConnector
from domain.company import Company
from domain.requirement import Requirement
from port.adapters.backoffice.projections.company_proj import CompanyProjection
from port.adapters.backoffice.projections.requirement_proj import RequirementsProjection
from port.adapters.persistence.model.company_sql_model import CompanySQLModel
from port.adapters.persistence.model.requirement_sql_model import RequirementSQLModel
from port.adapters.persistence.postgresql_executer import select, update


class PostgreSQLCompanyProjection(CompanyProjection):

    def save(self, company: Company, db_cursor: DbConnector = None) -> None:
        sql_template = (
            f"insert into {CompanySQLModel.table}"
            f"({CompanySQLModel.id_col}, {CompanySQLModel.name_col}, {CompanySQLModel.description_col}) "
            f"values"
            f"('{company.id}', '{company.name}', '{company.description}')"
        )
        update(cursor=db_cursor, sql_template=sql_template)

    def all(self, db_cursor: DbConnector = None) -> list[Company]:
        sql_template = f"select * from {CompanySQLModel.table}"
        return [Company(**i) for i in select(cursor=db_cursor, sql_template=sql_template)]
