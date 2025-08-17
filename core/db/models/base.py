import re

from sqlalchemy.orm import DeclarativeBase, declared_attr

from .mixins.base import BaseMixin

__all__ = [
    "Base",
]


def to_snake(camel: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel).lower()


class Base(BaseMixin, DeclarativeBase):
    @declared_attr
    def __tablename__(cls) -> str:
        return to_snake(cls.__name__)
