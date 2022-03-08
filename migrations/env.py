"""Модуль для работы с Alembic.

Обеспечивает подключение настроек alembic, подключение к БД из конфигов.
"""

import asyncio
from logging.config import fileConfig

from alembic import context as environment_context
from alembic.config import Config
from alembic.runtime.environment import EnvironmentContext
from sqlalchemy.future.engine import Connection

from app.db import get_connection_ctx
from app.db.base_model import Base
from app.models import *  # импортируются все модели, чтобы для всех моделей создавались миграции

# получение настроек из alembic.ini
context: EnvironmentContext = environment_context
config: Config = context.config

# Настройка логов из alembic.ini
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def do_run_migrations(connection: Connection) -> None:
    """Выполнить миграции."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    async with get_connection_ctx() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    raise RuntimeError("Unsupported operation. Online mode is available only.")

asyncio.run(run_migrations_online())
