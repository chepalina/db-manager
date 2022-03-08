# pylint: disable=invalid-name

from fastapi import Request, status
from fastapi.responses import JSONResponse, Response


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
