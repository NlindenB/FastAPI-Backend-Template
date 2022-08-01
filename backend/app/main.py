import fastapi as f
import uvicorn

from fastapi.middleware.cors import CORSMiddleware as FastAPICORSMiddleware

from app.utils.dashboard.admins import admin
from app.config.events import start_app_event_handler, terminate_app_event_handler
from app.config.settings import settings


def initialize_backend_app() -> f.FastAPI:
    app = f.FastAPI(**settings.fastapi_kwargs)

    app.add_middleware(
        FastAPICORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )
    app.add_event_handler("startup", start_app_event_handler(app=app))
    app.add_event_handler("shutdown", terminate_app_event_handler(app=app))
    # app.add_exception_handler()

    return app


app = initialize_backend_app()
admin = admin.initialize_sqladmin(app=app)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, log_level="info", reload=True)
