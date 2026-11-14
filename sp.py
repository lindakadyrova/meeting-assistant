import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

with open("data/transcripts/meeting01.txt", "r", encoding="utf-8") as f:
    text = f.read()

new_text =  text.replace("\n", " ")
newer_text = new_text.replace("\\n", " ")
newer_text =  newer_text.replace("interview's", "interview is")
# AI assistance was used to identify and handle an ambiguity in spaCy's tokenization and POS tagging. 
# In the phrase "interview's tomorrow", spaCy incorrectly interpreted `'s` as a possessive marker instead of the contraction "is". 
# AI helped identify this issue and develop a simple rule to replace "interview's" with "interview is" before processing the text.
doc = nlp(newer_text)
sents = list(doc.sents)


matcher = Matcher(nlp.vocab)

matcher.add("TO_GO", [[
    {"LEMMA": "be"},
    {"LEMMA": "go"},
    {"LOWER": "to"},
    {"POS": "VERB"}
]])

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print(span.sent.text)

