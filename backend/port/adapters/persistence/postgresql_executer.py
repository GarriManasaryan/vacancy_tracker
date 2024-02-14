from config.app import DbConnector, db_cursor_context


def select(sql_template: str, cursor: DbConnector) -> list[dict]:
    cursor.execute(sql_template)
    result = cursor.fetchall()
    return [dict(i) for i in result]


def update(sql_template: str, cursor: DbConnector) -> None:
    cursor.execute(sql_template)


def get_cursor() -> DbConnector:
    return db_cursor_context.get("db_cursor")
