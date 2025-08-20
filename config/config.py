from pathlib import Path

from orjson import dumps, loads
from pydantic import PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.db import Base


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    DEBUG: bool
    APP_HOST: str
    APP_PORT: PositiveInt
    APP_WORKERS: PositiveInt

    POSTGRES_DSN: str


settings = Settings()

async_database_engine = create_async_engine(
    url=settings.POSTGRES_DSN,
    json_deserializer=loads,
    json_serializer=dumps,
    pool_use_lifo=True,
    max_overflow=10,
    pool_size=50,
)

async_session_maker = async_sessionmaker(
    bind=async_database_engine, expire_on_commit=False, class_=AsyncSession
)


async def init_db():
    async with async_database_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables are already created!")
