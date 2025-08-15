from pydantic.alias_generators import to_snake
from sqlalchemy.orm import DeclarativeBase, declared_attr

from .mixins.base import BaseMixin

__all__ = [
    "Base",
]


class Base(BaseMixin, DeclarativeBase):
    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return to_snake(camel=cls.__name__)
