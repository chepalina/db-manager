from typing import TYPE_CHECKING, AsyncIterator

from app.db import get_session_ctx

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> AsyncIterator["AsyncSession"]:
    """Получить зависимость с сессией.

    Пример использования:
    ```
    @app.get('/ping')
    def ping(session: AsyncSession = Depends(get_session)):
        ...
    ```
    """
    async with get_session_ctx() as session:
        yield session
