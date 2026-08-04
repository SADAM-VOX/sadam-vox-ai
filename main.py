from fastapi import FastAPI

app = FastAPI(
    title="SADAM VOX AI",
    description="Artificial Intelligence Engine",
    version="0.1.0"
)


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
