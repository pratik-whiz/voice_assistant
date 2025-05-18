from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from src.services.stt_service import transcribe_audio
from src.services.tts_service import text_to_speech
from src.services.llm_service import query_phi3
from src.core.config import settings  # ✅ Ensure settings are used
import shutil
import os
import uuid

router = APIRouter()

# 1. STT Endpoint
@router.post("/stt")
async def stt_endpoint(file: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    try:
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        text = transcribe_audio(temp_filename)
        return {"transcription": text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

# 2. TTS Endpoint
@router.post("/tts")
async def tts_endpoint(text: str = Form(...)):
    lang = "hi" if any('\u0900' <= c <= '\u097F' for c in text) else "en"

    try:
        file_path = text_to_speech(text, lang)

        if file_path and os.path.exists(file_path):
            return FileResponse(
                path=file_path,
                filename=os.path.basename(file_path),
                media_type="audio/wav"
            )
        else:
            return JSONResponse(content={"error": "Failed to generate TTS file!"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# 3. LLM Endpoint
@router.post("/llm")
async def llm_endpoint(prompt: str = Form(...)):
    try:
        print(f"[LLM ROUTE] Using model: {settings.LLM_MODEL}")  # ✅ Debug check
        response = query_phi3(prompt)
        return {"response": response}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# 4. Conversation Endpoint
@router.post("/conversation")
async def conversation_endpoint(file: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}.wav"
    try:
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcription = transcribe_audio(temp_filename)
        print(f"[CONVERSATION] Transcribed: {transcription}")  # ✅ Debug

        print(f"[CONVERSATION] LLM Model in use: {settings.LLM_MODEL}")  # ✅ Confirm phi3 being used
        response_text = query_phi3(transcription)

        lang = "hi" if any('\u0900' <= c <= '\u097F' for c in response_text) else "en"
        file_path = text_to_speech(response_text, lang)

        if file_path and os.path.exists(file_path):
            return FileResponse(
                path=file_path,
                filename=os.path.basename(file_path),
                media_type="audio/wav"
            )
        else:
            return JSONResponse(content={"error": "TTS generation failed!"}, status_code=500)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
