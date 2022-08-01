import typing as t
import fastapi as f
import loguru as lg

from sqlalchemy import event

from app.database.db import Base, database


@event.listens_for(database.ENGINE.sync_engine, "connect")
def inspect_db_connection(dbapi_conn, conn_record):
    lg.logger.info(f"New DBAPI connection ---\n {dbapi_conn}")
    lg.logger.info(f"Connection record ---\n {conn_record}")


async def initialize_db_tables(conn) t.Awaitable: # type: ignore
    lg.logger.info("Table dropping --- Executing")
    await conn.run_sync(Base.metadata.drop_all)
    lg.logger.info("Table dropping --- Successful")

    lg.logger.info("Table creation --- Executing")
    await conn.run_sync(Base.metadata.create_all)
    lg.logger.info("Table creation --- Successfull")


async def initialize_db_connection(app: f.FastAPI) -> None:
    lg.logger.info("Database connection --- Establishing")

    app.state.pool = database.ENGINE

    async with app.state.pool.connect() as conn:
        await initialize_db_tables(conn)

    lg.logger.info("Database connection --- Established")


async def dispose_db_connection(app: f.FastAPI) -> None:
    lg.logger.info("Database connection --- Disposing")

    await app.state.pool.dispose()

    lg.logger.info("Database connection --- Disposed")
