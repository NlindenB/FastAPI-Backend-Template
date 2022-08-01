import typing as t

from functools import lru_cache

import decouple as d

from app.config.components.base import GlobalSettings
from app.config.components.development import DevSettings
from app.config.components.environment import Environment
from app.config.components.production import ProdSettings
from app.config.components.staging import StageSettings


class FactorySettings:
    def __init__(self, environment: t.Optional[str] = "DEV"):
        self.environment = environment

    def __call__(self) -> GlobalSettings:
        if self.environment == Environment.DEVELOPMENT.value:
            return DevSettings()
        elif self.environment == Environment.STAGING.value:
            return StageSettings()
        return ProdSettings()


@lru_cache()
def get_settings() -> GlobalSettings:
    return FactorySettings(d.config("ENV", default="DEV", cast=str))()  # type: ignore


settings = get_settings()
