from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):

    PROJECT_NAME: str = "SADAM VOX AI"

    VERSION: str = "1.0.0"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    STORAGE_PATH: Path = BASE_DIR / "storage"

    MODELS_PATH: Path = BASE_DIR / "models"

    TEMP_PATH: Path = BASE_DIR / "temp"

    LOGS_PATH: Path = BASE_DIR / "logs"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
