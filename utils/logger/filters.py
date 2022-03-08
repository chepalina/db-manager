from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from loguru import Record

# pylint: disable=disallowed-name


class RequireDebugTrueFilter:
    """Класс фильтра для loguru, пропускающий сообщения при debug==True."""

    def __init__(self, debug: bool):
        """Конструктор."""
        self.debug = debug

    def __call__(self, record: "Record") -> bool:
        """Операция вызова объекта как функции."""
        return self.debug


class RequireDebugFalseFilter:
    """Класс фильтра для loguru, пропускающий сообщения при debug==False."""

    def __init__(self, debug: bool):
        """Конструктор."""
        self.debug = debug

    def __call__(self, record: "Record") -> bool:
        """Операция вызова объекта как функции."""
        return not self.debug
