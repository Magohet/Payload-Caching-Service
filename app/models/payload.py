from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import mapped_column, Mapped

from config.config import async_database_engine
from core.db.models.base import Base

__all__ = [
    "Payload",
    "init_db"
]


class Payload(Base):
    __tablename__ = "payload"

    list_1: Mapped[list[str]] = mapped_column(ARRAY(String))
    list_2: Mapped[list[str]] = mapped_column(ARRAY(String))
    result: Mapped[str] = mapped_column(String)


async def init_db():
    async with async_database_engine.begin() as conn:
        await conn.run_sync(Payload.metadata.create_all)
    print("Таблицы созданы или уже существуют!")
