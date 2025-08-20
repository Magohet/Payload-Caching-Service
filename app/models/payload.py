from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, Mapped

from core.db.models.base import Base

__all__ = [
    "Payload",
]


class Payload(Base):
    __tablename__ = "payload"

    list_1: Mapped[list[str]] = mapped_column(ARRAY(String))
    list_2: Mapped[list[str]] = mapped_column(ARRAY(String))
    result: Mapped[str] = mapped_column(String)
