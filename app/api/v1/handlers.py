# pylint: disable=invalid-name
from fastapi import Request, status
from fastapi.applications import FastAPI
from fastapi.responses import JSONResponse, Response


def add_all_error_handlers(app: FastAPI) -> None:
    """Добавить все обработчики ошибок из данного роута к приложению.

    :param app: приложение FastAPI
    """
    app.add_exception_handler(Exception, unknown_error_handler)


async def unknown_error_handler(_: Request, exc: Exception) -> Response:
    """Обработчик всех ошибок.

        На случай, если при работе роута возникла ошибка, не обработанная другими хэндлерами.

    :param exc: исключение, обрабатываемое обработчиком
    :return: ответ сервера при получении обрабатываемой ошибки
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": str(exc)},
    )
