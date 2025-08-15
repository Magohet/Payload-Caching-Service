import uuid as uuid_pkg
from datetime import UTC, datetime
from typing import Optional

from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.orm import Mapped, mapped_column

__all__ = [
    "BaseMixin",
]


class BaseMixin:
    id: Mapped[uuid_pkg.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(tz=UTC),
        nullable=False,
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=lambda: datetime.now(tz=UTC),
        nullable=True,
    )
