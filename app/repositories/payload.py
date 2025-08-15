from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models import Payload
from app.schemas import PayloadCreateRequestDTO
from core.db.exceptions import (
    IntegrityConflictException,
    UnknownException,
    NotFoundException,
)
from core.db.repository import SQLAlchemyRepository
from core.deps import DBSession

__all__ = ["PayloadSQLRepository"]


class PayloadSQLRepository(SQLAlchemyRepository):
    async def create_payload(self, payload_data: PayloadCreateRequestDTO) -> Payload:
        try:
            payload = Payload(
                list_1=payload_data.list_1,
                list_2=payload_data.list_2,
                result=payload_data.result,
            )
            self._session.add(payload)
            return payload
        except IntegrityError:
            raise IntegrityConflictException(
                f"{Payload.__tablename__} conflicts with existing data.",
            )
        except Exception as e:
            raise UnknownException(f"Unknown error occurred: {e}") from e

    async def get_payload(
            self, payload_id: UUID
    ) -> Payload:
        query = select(Payload).where(Payload.id == payload_id)
        result = await self._session.execute(query)
        visit = result.scalar_one_or_none()
        if not visit:
            raise NotFoundException
        return visit


def get_payload_sql_repository(
        session: DBSession,
) -> PayloadSQLRepository:
    return PayloadSQLRepository(session)
