from uuid import UUID

from fastapi import APIRouter

from app.schemas import PayloadDTO, PayloadCreateResponseDTO, PayloadCreateRequestDTO
from app.services import PayloadServiceDeps

__all__ = ["router"]

router = APIRouter(tags=["payload"], prefix="/payload")


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@router.get("/{payload_id}", response_model=PayloadDTO)
async def get_payload(payload_id: UUID, service: PayloadServiceDeps):
    return await service.get_payload_by_id(payload_id)


@router.post("/", response_model=PayloadCreateResponseDTO)
async def create_payload(payload_data: PayloadCreateRequestDTO, service: PayloadServiceDeps):
    return await service.create_payload(payload_data)
