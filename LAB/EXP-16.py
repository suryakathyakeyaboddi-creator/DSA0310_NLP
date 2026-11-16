import spacy

nlp = spacy.load("en_core_web_sm")

text = ("Apple Inc. was founded by Steve Jobs in California in 1976. "
        "Sundar Pichai, the CEO of Google, visited Mumbai on 5 March 2024 "
        "and announced an investment of $2 billion in India.")

doc = nlp(text)
print(f"{'Entity':22s}{'Label':10s}Description")
for ent in doc.ents:
    print(f"{ent.text:22s}{ent.label_:10s}{spacy.explain(ent.label_)}")
