from uuid import UUID

from fastapi import APIRouter

__all__ = ["router"]
router = APIRouter(tags=["payload"], prefix="/payload")


@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@router.get("/payload/{payload_id}")  # ToDo: add dependencies + request/response model
async def get_payload(payload_id: UUID):
    return {"status": "ok"}


@router.post("/payload")  # ToDo: add dependencies + request/response model
async def create_payload():
    return {"status": "ok"}
