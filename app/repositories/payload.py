from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models import Payload
from app.schemas import PayloadCreateDTO
from core.db.exceptions import (
    IntegrityConflictException,
    UnknownException,
    NotFoundException,
)
from core.db.repository import SQLAlchemyRepository

__all__ = ["PayloadSQLRepository"]


class PayloadSQLRepository(SQLAlchemyRepository):
    async def create_payload(self, payload_data: PayloadCreateDTO) -> Payload:
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
            raise UnknownException(f"Unknown error occurred: {e}")

    async def get_payload_by_id(
            self, payload_id: UUID
    ) -> Payload:
        query = select(Payload).where(Payload.id == payload_id)
        result = await self._session.execute(query)
        visit = result.scalar_one_or_none()
        if not visit:
            raise NotFoundException(f"Resource {payload_id} not found")
        return visit

    async def get_payload_by_lists(
            self, list_1: List[str], list_2: List[str]
    ) -> Payload:
        query = select(Payload).where(Payload.list_1 == list_1, Payload.list_2 == list_2)
        result = await self._session.execute(query)
        visit = result.scalar_one_or_none()
        return visit
