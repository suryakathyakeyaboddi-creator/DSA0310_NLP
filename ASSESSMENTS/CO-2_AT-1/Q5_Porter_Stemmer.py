# Install NLTK once, if needed, using: pip install nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["relational", "relation", "relate"]

print("PORTER STEMMER-BASED PREPROCESSING")
print("-" * 42)
print(f"{'Original':<16}{'Porter stem':<16}")
print("-" * 42)

for word in words:
    print(f"{word:<16}{stemmer.stem(word):<16}")

print("-" * 42)
