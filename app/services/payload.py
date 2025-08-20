from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories import PayloadSQLRepository
from app.schemas import PayloadDTO, PayloadCreateRequestDTO, PayloadCreateDTO, PayloadCreateResponseDTO
from app.services.external_service import ExternalService
from core.deps import DBSession

__all__ = ["PayloadService", "PayloadServiceDeps", "get_payload_service"]


class PayloadService:
    def __init__(
            self,
            session: AsyncSession,
            repository: PayloadSQLRepository,
            external_service: ExternalService,
    ):
        self.session = session
        self.repository = repository
        self.external_service = external_service

    async def create_payload(self, request_data: PayloadCreateRequestDTO) -> PayloadCreateResponseDTO:
        payload = await self.repository.get_payload_by_lists(request_data.list_1, request_data.list_2)

        if not payload:
            transformed_list_1 = await self.external_service.transform(request_data.list_1)
            transformed_list_2 = await self.external_service.transform(request_data.list_2)

            result = []
            for a, b in zip(transformed_list_1, transformed_list_2):
                result.extend([a, b])

            payload_data = PayloadCreateDTO(
                list_1=request_data.list_1,
                list_2=request_data.list_2,
                result=str(result),
            )

            payload = await self.repository.create_payload(payload_data)
            await self.session.commit()
            await self.session.refresh(payload)

        response_data = PayloadCreateResponseDTO.model_validate(payload)

        return response_data

    async def get_payload_by_id(self, payload_id: UUID) -> PayloadDTO:
        payload = await self.repository.get_payload_by_id(payload_id)
        payload = PayloadDTO.model_validate(obj=payload)
        payload_data = payload.model_dump()

        return payload_data


def get_payload_service(session: DBSession) -> PayloadService:
    repository = PayloadSQLRepository(session)
    external_service = ExternalService()
    return PayloadService(session=session, repository=repository, external_service=external_service)


PayloadServiceDeps = Annotated[PayloadService, Depends(dependency=get_payload_service)]
