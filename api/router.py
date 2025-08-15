from fastapi import APIRouter

from api.payload import router as payload_router

__all__ = ["router"]

router = APIRouter(prefix="/api")

router.include_router(router=payload_router)
