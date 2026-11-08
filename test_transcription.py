from src.transcription import transcribe_audio, save_transcript


audio_path = "data/audio/test.mp3"

transcript = transcribe_audio(audio_path)
saved_path = save_transcript(transcript, audio_path)


print("\nTranskript:")
print(transcript)
print(f"Gespeichert unter: {saved_path}")