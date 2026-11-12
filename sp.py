import spacy
nip = spacy.load("en_core_web_sm")

with open("data/transcripts/meeting01.txt", "r", encoding="utf-8") as f:
    text = f.read()

new_text =  text.replace("\n", " ")
newer_text = new_text.replace("\\n", " ")
newer_text =  newer_text.replace("interview's", "interview is")
doc = nip(newer_text)
#print([(w.text, w.pos_) for w in doc])

for token in doc:
    if "'" in token.text or (
        token.pos_ == "ADP" and len(token.text) > len(token.lemma_)
    ):
        print(f"Verschmelzung/Kontraktion: {token.text} -> Lemma: {token.lemma_}")


# AI assistance was used to identify and handle an ambiguity in spaCy's tokenization and POS tagging. 
# In the phrase "interview's tomorrow", spaCy incorrectly interpreted `'s` as a possessive marker instead of the contraction "is". 
# AI helped identify this issue and develop a simple rule to replace "interview's" with "interview is" before processing the text.
