from app.config.components.base import GlobalSettings
from app.config.components.environment import Environment


class DevSettings(GlobalSettings):
    DESCRIPTION: str = """
    Environment:
    - Development
    
    Project Description
    - XYZ
    
    Team:
    - XYZ
    
    Objectives:
    - XYZ
    
    Techstack:
    - XYZ
    
    """
    DEBUG: bool = True
    ENV: Environment = Environment.DEVELOPMENT
