from typing import Type, TypeVar

import toml
from pydantic import BaseModel

from utils.base_dir import BASE_DIR

_PYPROJECT_FILENAME = "pyproject.toml"
_PYPROJECT_FILEPATH = BASE_DIR / _PYPROJECT_FILENAME

T = TypeVar("T", bound="PyProjectData")


class PoetryToolData(BaseModel):
    """Настройки pyproject.tool.poetry."""

    name: str
    version: str
    description: str
    authors: list[str]


class ToolsData(BaseModel):
    """Настройки pyproject.tool."""

    poetry: PoetryToolData


class PyProjectData(BaseModel):
    """Настройки проекта из pyproject.toml."""

    tool: ToolsData

    @classmethod
    def get_settings(cls: Type[T]) -> T:
        """Создать/вернуть синглтон класса PyProjectData."""
        return cls(**toml.load(_PYPROJECT_FILEPATH))
