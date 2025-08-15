from datetime import datetime
from typing import List
from uuid import UUID

from core.types import ImmutableDTO


class PayloadCreateRequestDTO(ImmutableDTO):
    list_1: List[str]
    list_2: List[str]


class PayloadCreateResponseDTO(ImmutableDTO):
    output: str


class PayloadDTO(ImmutableDTO):
    id: UUID
    list_1: List[str]
    list_2: List[str]
    result: str
    created_at: datetime
    updated_at: datetime
