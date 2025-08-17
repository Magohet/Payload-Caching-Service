from typing import Annotated

from fastapi import Depends

from config.config import async_session_maker
from core.db.models.session import AsyncSession

__all__ = [
    "DBSession",
]

async def create_database_session() -> AsyncSession:
    async with async_session_maker() as session:  # type: AsyncSession
        yield session


DBSession = Annotated[AsyncSession, Depends(dependency=create_database_session)]
