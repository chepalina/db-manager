from pydantic import BaseModel

from utils.pyproject import PyProjectData

PYPROJECT = PyProjectData.get_settings()


class AppSettings(BaseModel):
    """Настройки приложения."""

    # Имя среды
    tag: str = PYPROJECT.tool.poetry.name
    # Тег среды
    env: str = "PROD"
    # Версия приложения
    version: str = PYPROJECT.tool.poetry.version

    class Config:
        env_prefix = "app_"
