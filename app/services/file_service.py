from pathlib import Path
import shutil
import uuid

from app.core.config import settings


class FileService:

    def __init__(self):

        self.storage = settings.STORAGE_PATH

        self.storage.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, source: str) -> str:

        source = Path(source)

        extension = source.suffix

        filename = f"{uuid.uuid4()}{extension}"

        destination = self.storage / filename

        shutil.copy(source, destination)

        return str(destination)
