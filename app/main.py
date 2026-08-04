from fastapi import FastAPI

from app.api.voice import router as voice_router
from app.api.noise import router as noise_router

app = FastAPI(
    title="SADAM VOX AI",
    description="Artificial Intelligence Engine",
    version="0.1.0"
)

app.include_router(voice_router)
app.include_router(noise_router)


@app.get("/")
async def root():
    return {
        "name": "SADAM VOX AI",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
