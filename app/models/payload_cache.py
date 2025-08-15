from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base

__all__ = [
    "Payload",
]


class Payload(Base):
    list_1: Mapped[list[str]] = mapped_column(JSON)
    list_2: Mapped[list[str]] = mapped_column(JSON)
    result: Mapped[str] = mapped_column(String)
