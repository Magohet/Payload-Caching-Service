from typing import Annotated

from fastapi import Depends

from config.config import async_session_maker
from core.db.models.session import AsyncSession
from core.db.uow import SQLAlchemyUoW

__all__ = [
    "DBSession",
    "SQLUnitOfWorkDeps",
]


async def create_database_session() -> AsyncSession:
    async with async_session_maker() as session:  # type: AsyncSession
        yield session


DBSession = Annotated[AsyncSession, Depends(dependency=create_database_session)]


def get_sql_uow(session: DBSession) -> SQLAlchemyUoW:
    return SQLAlchemyUoW(session=session)


SQLUnitOfWorkDeps = Annotated[SQLAlchemyUoW, Depends(dependency=get_sql_uow)]
