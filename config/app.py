from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.router import router
from app.models import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await init_db()
    yield


app = FastAPI(debug=True, title="Caching Service", lifespan=lifespan)

app.include_router(router=router)
