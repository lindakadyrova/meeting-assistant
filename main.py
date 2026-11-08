from pathlib import Path
from src.transcription import transcribe_audio, save_transcript

user_input = input("Please enter the path to the audio file: ")

try:
    audio_path = Path(user_input).expanduser().resolve()

    transcript = transcribe_audio(str(audio_path))
    saved_path = save_transcript(transcript, str(audio_path))

    print("\nTranskript:")
    print(transcript)
    print(f"Gespeichert unter: {saved_path}")

except FileNotFoundError as error:
    print(f"Fehler: {error}")

except PermissionError as error:
    print(f"Keine Berechtigung zum Speichern: {error}")

except Exception as error:
    print(f"Unerwarteter Fehler: {error}")