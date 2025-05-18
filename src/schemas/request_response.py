from pydantic import BaseModel
from typing import Optional

class TextResponse(BaseModel):
    original_text: str
    corrected_text: str
    llm_response: str

class AudioResponse(TextResponse):
    audio_response: bytes
