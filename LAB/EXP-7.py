import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

text = "The quick brown fox jumps over the lazy dog near the river bank."
tokens = word_tokenize(text)
tags = nltk.pos_tag(tokens)

print(f"{'Word':10s}POS tag")
for word, tag in tags:
    print(f"{word:10s}{tag}")
