import typing as t
import fastapi as f
import loguru as lg

from app.database.events import dispose_db_connection, initialize_db_connection


def start_app_event_handler(app: f.FastAPI) -> t.Any:
    async def start_app_events() -> t.Coroutine[t.Any, t.Any, None]:  # type: ignore
        await initialize_db_connection(app)

    return start_app_events


def terminate_app_event_handler(app: f.FastAPI) -> t.Any:
    @lg.logger.catch
    async def terminate_app_events() -> None:
        await dispose_db_connection(app)

    return terminate_app_events
