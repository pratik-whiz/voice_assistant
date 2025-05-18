from TTS.utils.manage import ModelManager

# Initialize model manager
manager = ModelManager()

# Download TTS model
tts_path, config_path, _ = manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")

# Download vocoder model
vocoder_path, vocoder_config_path, _ = manager.download_model("vocoder_models/en/ljspeech/hifigan_v2")

print("✅ Downloaded TTS model to:", tts_path)
print("✅ Downloaded config to:", config_path)
print("✅ Downloaded vocoder model to:", vocoder_path)
print("✅ Downloaded vocoder config to:", vocoder_config_path)
