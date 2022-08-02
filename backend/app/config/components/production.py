from app.config.components.base import GlobalSettings
from app.config.components.environment import Environment


class ProdSettings(GlobalSettings):
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
    DEBUG: bool = False
    ENV: Environment = Environment.PRODUCTION
