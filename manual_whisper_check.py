from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

segments, info = model.transcribe("data/audio/test.mp3", language="de")

print("Erkannte Sprache:", info.language)
print("\nTranskript:")

for segment in segments:
    print(segment.text)