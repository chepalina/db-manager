from pydantic import BaseModel


class DBSettings(BaseModel):
    """Класс настройки подключения к базе данных."""

    url: str = 'sqlite:///:memory:'

    class Config:
        env_prefix = "db_"
