from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Application configuration settings
    Automatically loads values from .env file
    """

    # App Info
    APP_NAME: str = "Path2Place API"
    API_V1_PREFIX: str = "/api"

    # MongoDB
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "path2place_db"

    # JWT Authentication
    SECRET_KEY: str = "super-secret-key-change-this"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    # CORS
    FRONTEND_URL: str = "http://localhost:5173"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    """
    Returns cached settings object
    Prevents reloading environment variables repeatedly
    """
    return Settings()