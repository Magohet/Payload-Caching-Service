from fastapi import HTTPException
from starlette import status


class UnknownException(HTTPException):
    def __init__(self, message: str = "Unknown error occurred"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=[
                {
                    "type": "unknown_error",
                    "msg": message,
                }
            ],
        )


class IntegrityConflictException(HTTPException):
    def __init__(self, message: str = "Integrity Conflict"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=[
                {
                    "type": "integrity_error",
                    "msg": message,
                }
            ],
        )


class NotFoundException(HTTPException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[
                {
                    "type": "not_found",
                    "msg": message,
                }
            ],
        )
