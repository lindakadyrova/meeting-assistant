import src.transcription as transcription
from pathlib import Path

def test_save_transcript(monkeypatch):
    test_dir = Path("tests/test_output")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    monkeypatch.setattr(
        transcription,
        "Path",
        lambda path: test_dir if path == "data/transcripts" else Path(path)
    )

    transcript = "Hello, this is a test!"
    audio_path = "test_meeting.mp3"

    saved_path = transcription.save_transcript(transcript, audio_path)

    assert Path(saved_path).exists()
    assert Path(saved_path).read_text(encoding="utf8") == transcript