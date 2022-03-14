"""Database.

Для работы с базой данных используем sqlalchemy.
"""

from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import (AsyncConnection, AsyncEngine, AsyncSession,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base

from app.settings import DBSettings

Base = declarative_base()


@lru_cache()
def async_engine_singleton() -> AsyncEngine:
    """Создать синглтон асинхронного "движка" работы с базой данных.

    При первом вызове создается экземпляр класса `sqlalchemy.ext.asyncio.AsyncEngine`.
    При последующих вызовах возвращается прежде созданный экземпляр.

    :return: асинхронный "движок" работы с базой данных
    """
    config = DBSettings()

    engine: AsyncEngine = create_async_engine(
        url=config.url,
    )

    return engine


@asynccontextmanager
async def get_connection_ctx() -> AsyncIterator[AsyncConnection]:
    """Контекстный менеджер асинхронного подключения к БД.

    Так же задает схему БД по умолчанию.

    :yield: асинхронное соединение с БД
    """
    engine = async_engine_singleton()

    async with engine.begin() as conn:
        # задается схема по умолчанию
        # так же является местом внедрения зависимости от схемы
        # позволяет писать код моделей и миграций без привязки к схеме
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
