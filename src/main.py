from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router as api_router  # rename for clarity
from src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A FastAPI-based voice assistant with STT, LLM, and TTS capabilities",
    version="0.1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all API routes under single prefix
app.include_router(api_router, prefix=settings.API_V1_STR)
