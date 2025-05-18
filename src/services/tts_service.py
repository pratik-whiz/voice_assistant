import os
import uuid
import pyttsx3

# Initialize the TTS engine once
engine = None
try:
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Try to get a better voice if available
    voices = engine.getProperty('voices')
    for voice in voices:
        # Try to find an English voice by checking the name
        if voice.name and ('en' in voice.name.lower() or 'english' in voice.name.lower()):
            engine.setProperty('voice', voice.id)
            break
    
except Exception as e:
    print(f"Error initializing TTS engine: {str(e)}")
    raise

def text_to_speech(text: str, lang: str = "en") -> str:
    """Convert text to speech using pyttsx3 and return the path to the audio file"""
    try:
        # Validate input
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty.")

        if lang.lower() != "en":
            raise ValueError("This TTS model only supports English language.")

        # Generate unique filename and output directory
        output_dir = "output_audio"
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"tts_output_{uuid.uuid4().hex}.wav")

        # Generate speech and save to file
        engine.save_to_file(text, output_path)
        engine.runAndWait()

        return output_path

    except Exception as e:
        print(f"[TTS Error] {str(e)}")
        raise RuntimeError("TTS failed to generate audio.")
