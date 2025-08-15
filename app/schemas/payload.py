from datetime import datetime
from typing import List, Optional
from uuid import UUID

from core.types import ImmutableDTO, MutableDTO

__all__ = ["PayloadCreateRequestDTO", "PayloadCreateResponseDTO", "PayloadDTO"]


class PayloadCreateRequestDTO(MutableDTO):
    list_1: List[str]
    list_2: List[str]
    result: Optional[str]


class PayloadCreateResponseDTO(ImmutableDTO):
    output: str


class PayloadDTO(ImmutableDTO):
    id: UUID
    list_1: List[str]
    list_2: List[str]
    result: str
    created_at: datetime
    updated_at: datetime
