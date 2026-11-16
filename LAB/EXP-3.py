import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer, LancasterStemmer
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)

text = "The children were running faster than the studying students"
tokens = word_tokenize(text)
print("Tokens:", tokens, "\n")

stem, lanc, lem = PorterStemmer(), LancasterStemmer(), WordNetLemmatizer()
print(f"{'Word':10s}{'Porter':10s}{'Lancaster':11s}{'Lemma(noun)':13s}{'Lemma(verb)'}")
for w in tokens:
    print(f"{w:10s}{stem.stem(w):10s}{lanc.stem(w):11s}{lem.lemmatize(w):13s}{lem.lemmatize(w, pos='v')}")
