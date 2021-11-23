from typing import Optional

from pydantic import BaseSettings
from pydantic.networks import HttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = "cards"
    SENTRY_DSN: Optional[HttpUrl] = None


settings = Settings()
