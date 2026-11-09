import spacy
nip = spacy.load("en_core_web_sm")
doc = nip("I want to submit this project with anna this friday!")
print([(w.text, w.pos_) for w in doc])