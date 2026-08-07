from pydantic import BaseModel


class VoiceCloneRequest(BaseModel):
    voice_name: str


class VoiceCloneResponse(BaseModel):
    success: bool
    voice_id: str
    voice_name: str
