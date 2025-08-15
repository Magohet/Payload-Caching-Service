import logging

from typer import Typer
from uvicorn import run

from config.config import settings

__all__ = ["cli"]

logger = logging.getLogger(__name__)

cli = Typer(name="Caching Service")


@cli.command(name="run")
def _run():
    run(
        app="config.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        loop="uvloop",
        interface="asgi3",
        workers=settings.APP_WORKERS,
        log_level=logging.DEBUG,
    )
