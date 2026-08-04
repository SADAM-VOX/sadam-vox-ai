from fastapi import APIRouter, UploadFile, File

import tempfile

from app.engines.noise_engine import NoiseEngine

router = APIRouter(
    prefix="/noise",
    tags=["Noise Removal"]
)

engine = NoiseEngine()


@router.post("/remove")
async def remove_noise(file: UploadFile = File(...)):

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp.write(await file.read())
    temp.close()

    result = engine.process(temp.name)

    return {
        "status": "success",
        "output": result
    }
