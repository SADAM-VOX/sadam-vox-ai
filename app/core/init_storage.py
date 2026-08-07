from pathlib import Path

from app.core.config import settings


def initialize_storage():

    folders = [
        settings.STORAGE_PATH,
        settings.MODELS_PATH,
        settings.TEMP_PATH,
        settings.LOGS_PATH,
    ]

    for folder in folders:
        Path(folder).mkdir(
            parents=True,
            exist_ok=True
        )
