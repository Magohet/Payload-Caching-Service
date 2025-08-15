from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession as _AsyncSession

from .exception_handler import ExceptionDetail, SQLAlchemyExceptionParser

__all__ = [
    "AsyncSession",
    "ExceptionDetail",
]


class AsyncSession(_AsyncSession):
    async def commit(self, raise_exc: bool = False) -> ExceptionDetail | None:
        with SQLAlchemyExceptionParser() as e:
            await super().commit()

        if e.exception_detail:
            await super().rollback()
            if raise_exc:
                raise RequestValidationError(errors=e.exception_detail)

        return e.exception_detail
