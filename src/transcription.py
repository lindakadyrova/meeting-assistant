from faster_whisper import WhisperModel

def transcribe_audio(audio_path: str) -> str:
    model = WhisperModel("base", device="cpu", compute_type="int8")

    result = model.transcribe(audio_path, language="de")

    segments = result[0]
    info = result[1]

    transcript = " ".join(segment.text.strip() for segment in segments)

    print(f"Erkannte Sprache: {info.language}")

    return transcript