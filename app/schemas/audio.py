from pydantic import BaseModel


class AudioInfo(BaseModel):
    filename: str
    duration: float
    sample_rate: int
    channels: int


class AudioProcessResponse(BaseModel):
    success: bool
    input_file: str
    output_file: str
    processing_time: float
