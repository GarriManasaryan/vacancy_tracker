from config.app import DbConnector
from domain.company import Company
from domain.requirement import Requirement
from domain.salary import Salary
from port.adapters.backoffice.projections.company_proj import CompanyProjection
from port.adapters.backoffice.projections.requirement_proj import RequirementsProjection
from port.adapters.backoffice.projections.salary_proj import SalaryProjection
from port.adapters.persistence.model.salary_sql_model import SalarySQLModel
from port.adapters.persistence.model.requirement_sql_model import RequirementSQLModel
from port.adapters.persistence.postgresql_executer import select, update


class PostgreSQLSalaryProjection(SalaryProjection):

    def save(self, salary: Salary, db_cursor: DbConnector = None) -> None:
        sql_template = (
            f"insert into {SalarySQLModel.table}"
            f"({SalarySQLModel.id_col}, {SalarySQLModel.min_col}, {SalarySQLModel.max_col}) "
            f"values"
            f"('{salary.id}', '{salary.min}', '{salary.max}')"
        )
        update(cursor=db_cursor, sql_template=sql_template)

    def all(self, db_cursor: DbConnector = None) -> list[Salary]:
        sql_template = f"select * from {SalarySQLModel.table}"
        return [Salary(**i) for i in select(cursor=db_cursor, sql_template=sql_template)]
