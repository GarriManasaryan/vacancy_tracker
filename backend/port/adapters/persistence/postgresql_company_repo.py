from domain.company import Company
from domain.repo.company_repo import CompanyRepo
from port.adapters.persistence.model.company_sql_model import CompanySQLModel
from port.adapters.persistence.postgresql_executer import select, update, get_cursor


class PostgreSQLCompanyRepo(CompanyRepo):

    def save(self, company: Company) -> None:
        # не через self и инит, ибо мы один раз инициализируем класс, а при каждом вызове метода
        # чтобы взять конкретный курсор из потока-контекста
        cursor = get_cursor()
        sql_template = (
            f"insert into {CompanySQLModel.table}"
            f"({CompanySQLModel.id_col}, {CompanySQLModel.name_col}, {CompanySQLModel.description_col}) "
            f"values"
            f"('{company.id}', '{company.name}', '{company.description}')"
        )
        update(cursor=cursor, sql_template=sql_template)

    def all(self) -> list[Company]:
        cursor = get_cursor()
        sql_template = f"select * from {CompanySQLModel.table}"
        return [Company(**i) for i in select(cursor=cursor, sql_template=sql_template)]
