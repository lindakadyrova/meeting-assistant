from src.transcription import transcribe_audio

audio_path = "data/audio/test.mp3"

transcript = transcribe_audio(audio_path)

print("\nTranskript:")
print(transcript)