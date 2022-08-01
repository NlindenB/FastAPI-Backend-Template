from app.config.components.base import GlobalSettings
from app.config.components.environment import Environment


class ProdSettings(GlobalSettings):
    DESCRIPTION: str = "Backend application with production settings"
    DEBUG: bool = False
    ENV: Environment = Environment.PRODUCTION
