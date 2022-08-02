"""
Base Repository provides the connection attribute for the
database connection to execute the queries via C.R.U.D. methods.
"""

from sqlalchemy.ext.asyncio import AsyncConnection


class BaseRepository:
    def __init__(self, conn: AsyncConnection) -> None:
        self._conn = conn

    @property
    def connection(self) -> AsyncConnection:
        return self._conn
