"""Database.

Для работы с базой данных используем sqlalchemy.
"""

from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from app.settings import DBSettings

from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

BaseModel = declarative_base()


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@lru_cache()
def async_engine_singleton() -> Engine:
    """Создать синглтон асинхронного "движка" работы с базой данных.

    При первом вызове создается экземпляр класса `sqlalchemy.ext.asyncio.AsyncEngine`.
    При последующих вызовах возвращается прежде созданный экземпляр.

    :return: асинхронный "движок" работы с базой данных.
    """
    config = DBSettings()
    engine = create_engine(
        url=config.url
        , connect_args={"check_same_thread": False}
    )

    return engine


@asynccontextmanager
async def get_connection_ctx() -> AsyncIterator[AsyncConnection]:
    """Контекстный менеджер асинхронного подключения к БД.

    Так же задает схему БД по умолчанию.

    :yield: асинхронное соединение с БД.
    """
    engine = async_engine_singleton()

    async with engine.begin() as conn:
        yield conn


@asynccontextmanager
async def get_session_ctx() -> AsyncIterator[AsyncSession]:
    """Контекстный менеджер асинхронной сессии работы с БД.

    Так же задает схему БД по умолчанию.

    :yield: асинхронная сессия работы с БД.
    """
    async with get_connection_ctx() as connection:
        async with AsyncSession(bind=connection) as session:
            yield session
