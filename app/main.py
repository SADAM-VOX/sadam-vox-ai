from fastapi import FastAPI

from app.api.voice import router as voice_router

app = FastAPI(
    title="SADAM VOX AI",
    version="0.1.0"
)

app.include_router(voice_router)


@app.get("/")
def root():
    return {
        "project": "SADAM VOX AI",
        "status": "running"
    }
