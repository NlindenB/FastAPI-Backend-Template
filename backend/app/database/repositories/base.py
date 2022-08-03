"""
Base Repository provides the session attribute for the
ORM session to execute the queries via C.R.U.D. methods.
"""

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session: AsyncSession = session

    @property
    def session(self) -> AsyncSession:
        return self._session
