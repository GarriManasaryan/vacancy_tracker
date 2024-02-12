from config.app import DbConnector


def select(sql_template: str, cursor: DbConnector) -> list[dict]:
    cursor.execute(sql_template)
    result = cursor.fetchall()
    return [dict(i) for i in result]


def update(sql_template: str, cursor: DbConnector) -> None:
    cursor.execute(sql_template)
