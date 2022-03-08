from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session_ctx


async def get_session() -> AsyncIterator[AsyncSession]:

    async with get_session_ctx() as session:
        yield session
