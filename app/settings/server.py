from pydantic import BaseModel


class ServerSettings(BaseModel):
    """Настройки uvicorn сервера."""

    # Путь до ASGI в формате "<module>:<attribute>"
    app: str = "app.main:app"
    # Количество воркеров сервера
    workers: int = 1
    # Флаг запуска сервера в режиме разработки
    debug: bool = False
    # Уровень логирования
    log_level: str = "info"
    # Хост приложения
    host: str = "0.0.0.0"
    # Порт приложения
    port: int = 59999

    class Config:
        env_prefix = "server_"
