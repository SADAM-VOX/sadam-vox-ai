from pathlib import Path

from loguru import logger

from app.core.config import settings


Path(settings.LOGS_PATH).mkdir(
    parents=True,
    exist_ok=True
)

logger.remove()

logger.add(
    settings.LOGS_PATH / "sadam_vox.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO"
)
