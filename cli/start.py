import click
from uvicorn import Config, Server

from app.settings.server import ServerSettings
from utils.logger.config import setup_logging


@click.group()
def start() -> None:
    """Запустить один из выбранных сервисов."""
    pass


@start.command()
def api() -> None:
    """API-сервис."""
    server_settings: ServerSettings = ServerSettings()

    server = Server(
        Config(
            **server_settings.dict(),
        )
    )

    # Настроить логирование
    setup_logging(server_settings.log_level, server_settings.debug)

    # Запустить сервер
    server.run()
