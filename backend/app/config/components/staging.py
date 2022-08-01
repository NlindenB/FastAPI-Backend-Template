from app.config.components.base import GlobalSettings
from app.config.components.environment import Environment


class StageSettings(GlobalSettings):
    DESCRIPTION: str = "Backend application with staging settings"
    DEBUG: bool = True
    ENV: Environment = Environment.STAGING
    TEST_DATABASE_URI: str = "sqlite:///./my_db.sqlite3"
