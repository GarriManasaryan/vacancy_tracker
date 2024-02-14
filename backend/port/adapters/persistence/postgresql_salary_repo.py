from domain.repo.salary_repo import SalaryRepo
from domain.salary import Salary
from port.adapters.persistence.model.salary_sql_model import SalarySQLModel
from port.adapters.persistence.postgresql_executer import select, update, get_cursor


class PostgreSQLSalaryRepo(SalaryRepo):

    def save(self, salary: Salary) -> None:
        cursor = get_cursor()
        sql_template = (
            f"insert into {SalarySQLModel.table}"
            f"({SalarySQLModel.id_col}, {SalarySQLModel.min_col}, {SalarySQLModel.max_col}) "
            f"values"
            f"('{salary.id}', '{salary.min}', '{salary.max}')"
        )
        update(cursor=cursor, sql_template=sql_template)

    def all(self) -> list[Salary]:
        cursor = get_cursor()
        sql_template = f"select * from {SalarySQLModel.table}"
        return [Salary(**i) for i in select(cursor=cursor, sql_template=sql_template)]
