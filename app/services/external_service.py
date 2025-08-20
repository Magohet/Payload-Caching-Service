import asyncio
from typing import List, Annotated

from fastapi import Depends

__all__ = ["ExternalService", "PayloadServiceDeps", "get_external_service"]


class ExternalService:

    @staticmethod
    async def transform(list_1: List[str], list_2: List[str]) -> str:
        result = []
        for a, b in zip(list_1, list_2):
            result.extend([a, b])

        await asyncio.sleep(0.1)

        return str(result)


def get_external_service() -> ExternalService:
    return ExternalService()


PayloadServiceDeps = Annotated[ExternalService, Depends(dependency=get_external_service)]
