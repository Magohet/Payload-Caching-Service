from datetime import datetime
from typing import List, Optional
from uuid import UUID

from core.types import ImmutableDTO, MutableDTO

__all__ = ["PayloadCreateDTO", "PayloadCreateRequestDTO", "PayloadCreateResponseDTO", "PayloadDTO"]


class PayloadCreateDTO(MutableDTO):
    list_1: List[str]
    list_2: List[str]
    result: Optional[str]


class PayloadCreateRequestDTO(MutableDTO):
    list_1: List[str]
    list_2: List[str]


class PayloadCreateResponseDTO(ImmutableDTO):
    id: UUID


class PayloadDTO(ImmutableDTO):
    id: UUID
    list_1: List[str]
    list_2: List[str]
    result: str
    created_at: datetime
    updated_at: datetime
