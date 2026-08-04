from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.engines.voice_enhancer import VoiceEnhancer

router = APIRouter(prefix="/voice", tags=["Voice"])

enhancer = VoiceEnhancer()


@router.post("/enhance")
async def enhance_voice(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as input_file:
        input_file.write(await file.read())
        input_path = input_file.name

    output_path = input_path.replace(".wav", "_enhanced.wav")

    result = enhancer.enhance(input_path, output_path)

    return result
