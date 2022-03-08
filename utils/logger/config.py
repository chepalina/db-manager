import json
import logging
import sys
from typing import TYPE_CHECKING

from loguru import logger

from utils.logger.filters import RequireDebugFalseFilter, RequireDebugTrueFilter

if TYPE_CHECKING:
    from loguru import Message, Record

# pylint: disable=disallowed-name


class _InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = logging.getLevelName(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2

        while frame.f_code.co_filename == logging.__file__:
            depth += 1
            if frame.f_back is None:
                break

            frame = frame.f_back

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def _serialize(record: "Record") -> str:
    """Сериализовать информацию из лог-сообщения в json.

    :param record: информация из лог-сообщения
    :return: json строка
    """
    subset = {"level": record["level"].name, "message": record["message"]}
    return json.dumps(subset)


def _sink(message: "Message") -> None:
    """Вывести в stdout лог-сообщение.

    :param message: лог-сообщение
    """
    serialized = _serialize(message.record)
    print(serialized, file=sys.stdout)


def setup_logging(log_level: str, debug: bool) -> None:
    """Настроить логирование.

    Оставляем один логгер root, все лог-сообщения обрабатываются им.
    Оставляем два логгера: для разработки и для боевого сервера.

    :param log_level: уровень логирования
    :param debug: для запуска сервера в режиме разработки
    """
    # Intercept everything at the root logger
    logging.root.handlers = [_InterceptHandler()]
    logging.root.setLevel(log_level.upper())

    # Remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    # Configure Loguru
    logger.configure(
        handlers=[
            {
                "sink": _sink,
                "filter": RequireDebugFalseFilter(debug),
            },
            {
                "sink": sys.stdout,
                "colorize": True,
                "filter": RequireDebugTrueFilter(debug),
                "format": "<k><b>{level}</b></k> - {message}",
            },
        ]
    )
