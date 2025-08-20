import asyncio
from typing import Annotated, List

from fastapi import Depends

__all__ = ["ExternalService", "PayloadServiceDeps", "get_external_service"]


class ExternalService:

    @staticmethod
    async def transform(input_list: List[str]) -> List[str]:
        await asyncio.sleep(0.1)    # simulating external service request
        return [el.upper() for el in input_list]


def get_external_service() -> ExternalService:
    return ExternalService()


PayloadServiceDeps = Annotated[ExternalService, Depends(dependency=get_external_service)]
