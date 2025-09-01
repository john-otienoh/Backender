import secrets
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Blog"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "Simple Blog API"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False


settings = Settings()
