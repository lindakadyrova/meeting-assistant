import spacy
nip = spacy.load("en_core_web_sm")

with open("data/transcripts/meeting01.txt", "r", encoding="utf-8") as f:
    text = f.read()

new_text =  text.replace("\n", " ")
newer_text = new_text.replace("\\n", " ")
doc = nip(newer_text)
print([(w.text, w.pos_) for w in doc])