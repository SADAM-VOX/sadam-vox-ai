from pydantic import BaseModel
from datetime import datetime


class APIResponse(BaseModel):
    success: bool
    message: str


class HealthResponse(BaseModel):
    project: str
    version: str
    status: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: str


class TimeStamp(BaseModel):
    created_at: datetime
