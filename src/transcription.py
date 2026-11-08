from faster_whisper import WhisperModel
from pathlib import Path

def transcribe_audio(audio_path: str) -> str:
    if not Path(audio_path).exists():
          raise FileNotFoundError(f"Audiodatei nciht gefunden: {audio_path}")
    model = WhisperModel("base", device="cpu", compute_type="int8")

    result = model.transcribe(audio_path, language="de")

    segments = result[0]
    info = result[1]

    transcript = "\n".join(segment.text.strip() for segment in segments)

    print(f"Erkannte Sprache: {info.language}")


  
    return transcript

def save_transcript(transcript: str, audio_path: str) ->str:
      output_dir = Path("data/transcripts")
      output_dir.mkdir(parents=True, exist_ok=True)
    
      base_path = output_dir / f"{Path(audio_path).stem}.txt"
      output_path = base_path
    
      counter = 1
      while output_path.exists():
            output_path= output_dir / f"{Path(audio_path).stem}({counter}).txt"
            counter += 1
    
      with open(output_path, "w", encoding ="utf-8") as datei:
            datei.write(transcript)
    
      return str(output_path)