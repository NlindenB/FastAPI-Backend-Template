import logging as l
import typing as t

import decouple as d
import pydantic as p

from app.config.components.environment import Environment


class GlobalSettings(p.BaseSettings):
    """
    The main class for re-set up the Fastapi application with 3 possible environments.
    """

    TITLE: str = "YOUR_TITLE"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    ENV: Environment = d.config("ENV", default="DEV", cast=str)  # type: ignore
    DESCRIPTION: str
    DEBUG: bool

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    DB_HOST: str = "0.0.0.0"
    DB_ECHO_LOG: bool = False
    DB_FORCE_ROLLBACK: bool = False
    DB_POOL_SIZE: int = 50
    DB_POOL_OVERFLOW: int = 30
    DB_PORT: int = 5432
    DATABASE_URI: str = d.config("DATABASE_URI", cast=str)  # type: ignore

    JWT_TOKEN_PREFIX: str = d.config("JWT_TOKEN_PREFIX", cast=str)  # type: ignore
    SECRET_KEY: str = d.config("SECRET_KEY", cast=str)  # type: ignore

    ALLOWED_CREDENTIALS: bool = True
    ALLOWED_ORIGINS: t.List[str] = ["*"]
    ALLOWED_METHODS: t.List[str] = ["*"]
    ALLOWED_HEADERS: t.List[str] = ["*"]

    LOGGING_LEVEL: int = l.INFO
    LOGGERS: t.Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        """
        A Meta Class to setup Pydantic base configuration attributes.
        """

        case_sensitive: bool = True
        env_file: str = "backend/.env"
        validate_assignment: bool = True

    @property
    def fastapi_kwargs(self) -> t.Dict[str, t.Any]:
        """
        Returns dictionary-type values for substituting the FastAPI attributes via mapping method.
        """

        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }

    @property
    def set_async_database(self) -> t.Optional[str]:
        """
        Returns the asyncpg database schema if using async engine.
        """

        return (
            self.DATABASE_URI.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URI
            else self.DATABASE_URI
        )
