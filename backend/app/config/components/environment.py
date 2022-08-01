# type: ignore
import enum as e


class Environment(e.Enum):
    DEVELOPMENT: str = "DEV"
    PRODUCTION: str = "PROD"
    STAGING: str = "STAGE"
