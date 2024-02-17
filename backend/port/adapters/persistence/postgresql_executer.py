from typing import Generic, T

from fastapi import HTTPException

from config.app import DbConnector, db_cursor_context


def select(sql_template: str, cursor: DbConnector) -> list[dict]:
    cursor.execute(sql_template)
    result = cursor.fetchall()
    return [dict(i) for i in result]


def update(sql_template: str, cursor: DbConnector) -> None:
    try:
        cursor.execute(sql_template)
    except Exception as e:
        message = repr(e)
        if 'violates foreign key constraint' in repr(e):
            message = "Foreign key violation"
        raise HTTPException(status_code=404, detail=message)


def get_cursor() -> DbConnector:
    return db_cursor_context.get("db_cursor")


def all_entities(table: str, entity: Generic[T]) -> Generic[T]:
    cursor = get_cursor()
    sql_template = f"select * from {table}"
    return [entity(**i) for i in select(cursor=cursor, sql_template=sql_template)]
