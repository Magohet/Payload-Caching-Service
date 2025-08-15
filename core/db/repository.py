from core.db.models.session import AsyncSession


class SQLAlchemyRepository:
    def __init__(self, session: AsyncSession):
        self._session = session
