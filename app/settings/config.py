from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(env='DATABASE_URL')
    # environment: str = os.getenv('ENVIRONMENT', 'dev')
    # testing: bool = os.getenv('TESTING', 0)


settings = Settings()
