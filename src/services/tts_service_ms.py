# import os
# import uuid
# from pathlib import Path
# import torch
# from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
# import soundfile as sf

# # Initialize TTS with Microsoft's SpeechT5 model
# try:
#     processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
#     model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
#     vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
# except Exception as e:
#     print(f"Error initializing TTS: {str(e)}")
#     raise

# def text_to_speech(text: str, lang: str = "en") -> str:
#     try:
#         # Validate input
#         if not text or not text.strip():
#             raise ValueError("Input text cannot be empty.")

#         if lang.lower() != "en":
#             raise ValueError("This TTS model only supports English language.")

#         # Generate unique filename and output directory
#         output_dir = Path("output_audio")
#         output_dir.mkdir(exist_ok=True)
        
#         output_path = str(output_dir / f"tts_output_{uuid.uuid4().hex}.wav")

#         # Process text input
#         inputs = processor(text=text, return_tensors="pt")

#         # Generate speech without speaker embeddings (using default voice)
#         speech = model.generate_speech(
#             inputs["input_ids"],
#             vocoder=vocoder
#         )
        
#         # Save the audio file
#         sf.write(output_path, speech.numpy(), samplerate=16000)

#         return output_path

#     except Exception as e:
#         print(f"[TTS Error] {str(e)}")
#         raise RuntimeError("TTS failed to generate audio.")
