import os
import whisper

# Load the Whisper model (using base model for good balance of accuracy and speed)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe audio file to text using Whisper model
    
    Args:
        file_path (str): Path to the audio file to transcribe
        
    Returns:
        str: Transcribed text
    
    Raises:
        RuntimeError: If transcription fails
    """
    try:
        # Verify file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")

        # Transcribe with English forced
        result = model.transcribe(
            file_path,
            language="en",
            task="transcribe",
            fp16=False,
            verbose=False
        )

        # Extract and return the transcribed text
        transcribed_text = result["text"].strip()
        
        if not transcribed_text:
            raise ValueError("No speech detected in the audio file")
            
        return transcribed_text

    except Exception as e:
        print(f"STT Error: {str(e)}")
        raise RuntimeError("STT failed during transcription.")
