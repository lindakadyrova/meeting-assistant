from src.transcription import transcribe_audio, save_transcript


audio_path = "data/audio/tes.mp3"

try:
 transcript = transcribe_audio(audio_path)
 saved_path = save_transcript(transcript, audio_path)


 print("\nTranskript:")
 print(transcript)
 print(f"Gespeichert unter: {saved_path}")

except FileNotFoundError as error:
 print(f"Fehler: {error}")
 
except PermissionError as error:
 print(f"Keine Berechtigung zum Speichern: {error}")