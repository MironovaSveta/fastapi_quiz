import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = os.getenv('DATABASE_URL', '')


settings = Settings()
