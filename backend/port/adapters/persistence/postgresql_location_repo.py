from domain.location import Location
from domain.repo.location_repo import LocationRepo
from port.adapters.persistence.model.location_sql_model import LocationSQLModel
from port.adapters.persistence.postgresql_executer import get_cursor, update, select


class PostgreSQLLocationRepo(LocationRepo):
    def save(self, location: Location) -> None:
        cursor = get_cursor()
        sql_template = f"""
        insert into {LocationSQLModel.table} 
        ({LocationSQLModel.id}, {LocationSQLModel.country}, {LocationSQLModel.state}, {LocationSQLModel.city})
        values 
        ('{location.id}', '{location.country}', '{str(location.state)}', '{location.city}')
        """
        if not location.state:
            sql_template = sql_template.replace(
                f", '{str(location.state)}'", ""
            ).replace(f", {LocationSQLModel.state}", "")
        update(cursor=cursor, sql_template=sql_template)

    def all(self) -> list[Location]:
        cursor = get_cursor()
        sql_template = f"select * from {LocationSQLModel.table}"
        return [Location(**i) for i in select(cursor=cursor, sql_template=sql_template)]
