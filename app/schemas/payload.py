from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import StrictStr

from core.types import ImmutableDTO, MutableDTO

__all__ = ["PayloadCreateDTO", "PayloadCreateRequestDTO", "PayloadCreateResponseDTO", "PayloadDTO"]


class PayloadCreateDTO(MutableDTO):
    list_1: List[str]
    list_2: List[str]
    result: Optional[str]


class PayloadCreateRequestDTO(MutableDTO):
    list_1: List[StrictStr]
    list_2: List[StrictStr]


class PayloadCreateResponseDTO(ImmutableDTO):
    id: UUID
    result: str


class PayloadDTO(ImmutableDTO):
    id: UUID
    list_1: List[str]
    list_2: List[str]
    result: str
    created_at: datetime
    updated_at: Optional[datetime] = None
