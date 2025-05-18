import torch
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Voice Assistant API"

    USE_GPU: bool = torch.cuda.is_available()
    BATCH_SIZE: int = 1
    MAX_AUDIO_LENGTH: int = 30

    STT_MODEL: str = "openai/whisper-base"
    TTS_MODEL: str = "microsoft/speecht5_tts"

    # ✅ Alias used to map env variable "OLLAMA_MODEL"
    LLM_MODEL: str = Field("phi3", alias="OLLAMA_MODEL")

    # ✅ Alias used to map env variable "OLLAMA_SERVER_URL"
    OLLAMA_BASE_URL: str = Field("http://localhost:11434", alias="OLLAMA_SERVER_URL")

    SAMPLE_RATE: int = 16000
    MAX_TEXT_LENGTH: int = 512

    API_KEY: str | None = None

    ENABLE_ASYNC_PROCESSING: bool = True
    WORKER_COUNT: int = 2

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"  # Or use "allow" to accept unknown env vars

settings = Settings()

print("✅ Loaded OLLAMA_MODEL:", settings.LLM_MODEL)
print("✅ Loaded OLLAMA_SERVER_URL:", settings.OLLAMA_BASE_URL)
