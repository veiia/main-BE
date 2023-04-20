import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(
        default=os.getenv(
            "DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres"
        )
    )
    # environment: str = os.getenv('ENVIRONMENT', 'dev')
    # testing: bool = os.getenv('TESTING', 0)


settings = Settings()
