import sqlalchemy as sa
import typing as t
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

from app.config.settings import settings


class Database:
    ENGINE: AsyncEngine = create_async_engine(
        settings.set_async_database,
        echo=settings.DB_ECHO_LOG,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_POOL_OVERFLOW,
        poolclass=QueuePool,
    )
    SESSION: AsyncSession = sessionmaker(ENGINE, expire_on_commit=False, class_=AsyncSession)  # type: ignore


class Base(object):  # type: ignore
    id: uuid.UUID = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # type: ignore


database: t.Type[Database] = Database
Base: t.Any = declarative_base(cls=Base)
