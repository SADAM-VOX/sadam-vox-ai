from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "SADAM VOX AI"
    APP_VERSION: str = "0.1.0"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
