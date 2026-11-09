import src.transcription as transcription
from pathlib import Path

def test_save_transcript(monkeypatch, tmp_path):
    monkeypatch.setattr(
        transcription,
        "Path",
        lambda path: tmp_path if path == "data/transcripts" else Path(path)
    )

    transcript = "Hello, this is a test!"
    audio_path = "test_meeting.mp3"

    saved_path = transcription.save_transcript(transcript, audio_path)

    assert Path(saved_path).exists()
    assert Path(saved_path).read_text(encoding="utf-8") == transcript


def test_save_transcript_increments_filename(monkeypatch, tmp_path):
    monkeypatch.setattr(
        transcription,
        "Path",
        lambda path: tmp_path if path == "data/transcripts" else Path(path)
    )

    audio_path = "test_meeting.mp3"
    transcript = "Second test transcript."

    (tmp_path / "test_meeting.txt").write_text("First transcript")
    (tmp_path / "test_meeting(1).txt").write_text("Second transcript")
    (tmp_path / "test_meeting(2).txt").write_text("Third transcript")

    saved_path = transcription.save_transcript(transcript, audio_path)

    assert Path(saved_path).name == "test_meeting(3).txt"
    assert Path(saved_path).read_text(encoding="utf-8") == transcript

    print(tmp_path)