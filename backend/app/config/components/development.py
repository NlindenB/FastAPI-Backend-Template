from app.config.components.base import GlobalSettings
from app.config.components.environment import Environment


class DevSettings(GlobalSettings):
    DESCRIPTION: str = "Backend application with development settings"
    DEBUG: bool = True
    ENV: Environment = Environment.DEVELOPMENT
