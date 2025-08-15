from pydantic import BaseModel

__all__ = [
    "ExceptionDetail",
]


class ExceptionDetail(BaseModel):
    type: str
    msg: str
