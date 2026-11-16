import nltk
from nltk.corpus import wordnet as wn, stopwords
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk

for pkg in ["wordnet", "omw-1.4", "punkt", "punkt_tab", "stopwords"]:
    nltk.download(pkg, quiet=True)
stop = set(stopwords.words("english"))

def simple_lesk(word, sentence):
    """Pick the sense whose definition + examples overlap most with the context."""
    context = {w.lower() for w in word_tokenize(sentence) if w.isalpha()} - stop - {word}
    best, best_score = None, -1
    for sense in wn.synsets(word, pos=wn.NOUN):
        signature = set(word_tokenize(sense.definition().lower()))
        for ex in sense.examples():
            signature |= set(word_tokenize(ex.lower()))
        score = len((signature - stop) & context)
        if score > best_score:
            best, best_score = sense, score
    return best, best_score

sentences = [
    "I went to the bank to deposit my money and cash a check",
    "He sat on the bank of the river and watched the water flow",
]
for s in sentences:
    sense, score = simple_lesk("bank", s)
    print("Sentence :", s)
    print(f"Sense    : {sense.name()}  (overlap = {score})")
    print("Meaning  :", sense.definition())
    print("NLTK lesk:", lesk(word_tokenize(s), "bank", "n").name())
    print()
