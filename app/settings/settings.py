from typing import Any, Mapping, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str

    POSTGRES_URL: str = ""

    @validator("POSTGRES_URL", pre=True)
    def assemble_postgres_db_url(
        cls, v: Optional[str], values: Mapping[str, Any]
    ) -> Any:
        if v and isinstance(v, str):
            return v

        return str(
            PostgresDsn.build(
                scheme="postgresql",
                user=values["POSTGRES_USER"],
                password=values["POSTGRES_PASSWORD"],
                host=values["POSTGRES_HOST"],
                path=f'/{values["POSTGRES_DB"]}',
            )
        )


settings = Settings()
