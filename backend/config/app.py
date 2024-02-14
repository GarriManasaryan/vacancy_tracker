from contextvars import ContextVar
from dataclasses import dataclass
from os import getenv
from typing import Type, ContextManager, Callable, Optional

import psycopg2.extras
from psycopg2._psycopg import cursor
from psycopg2.pool import SimpleConnectionPool
from sqlalchemy import NullPool


connection_pool = SimpleConnectionPool(
    2, 12, user=getenv("POSTGRESQL_USER"), password=getenv("POSTGRESQL_PASSWORD"),
    host=getenv("POSTGRESQL_HOST"), port=getenv("POSTGRESQL_PORT"), database=getenv("POSTGRESQL_DB_NAME"))

DbConnector = cursor
db_cursor_context: ContextVar[Optional[DbConnector]] = ContextVar("db_cursor", default=None)


@dataclass
class Configuration:
    postgresql_host = getenv("POSTGRESQL_HOST")
    postgresql_port = getenv("POSTGRESQL_PORT")
    postgresql_db_name = getenv("POSTGRESQL_DB_NAME")
    postgresql_user = getenv("POSTGRESQL_USER")
    postgresql_password = getenv("POSTGRESQL_PASSWORD")

    engine_echo = False
    engine_pool_size: int | None = 50
    engine_pool_pre_ping = True
    engine_poolclass: Type[NullPool] | None = None

    upgrade_database = True

    @property
    def database_uri(self):
        return f"postgresql+psycopg2://{self.postgresql_user}:{self.postgresql_password}@{self.postgresql_host}:{self.postgresql_port}/{self.postgresql_db_name}"

    @property
    def engine_config(self):
        if self.engine_poolclass == NullPool:
            key = "poolclass"
            value = self.engine_poolclass
        else:
            key = "pool_size"
            value = self.engine_pool_size

        return {
            "echo": self.engine_echo,
            "pool_pre_ping": self.engine_pool_pre_ping,
            key: value,
        }


def get_config() -> Configuration:
    return Configuration()


class ConnectionFromPool:

    def __init__(self):
        self.connection_pool = None
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
