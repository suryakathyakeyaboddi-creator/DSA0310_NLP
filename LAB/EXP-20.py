import math
import re
from collections import Counter

docs = {
    "D1": "Natural language processing helps computers understand human language",
    "D2": "Machine learning models learn patterns from data",
    "D3": "Language models are trained on large text data for natural language tasks",
    "D4": "The football team won the match last night",
}
stop = {"the", "for", "on", "from", "are", "a", "of", "and"}

def tokens(text):
    return [w for w in re.findall(r"[a-z]+", text.lower()) if w not in stop]

tok = {d: tokens(t) for d, t in docs.items()}
N = len(docs)
df = Counter(w for ws in tok.values() for w in set(ws))
idf = {w: math.log10(N / df[w]) for w in df}

def tfidf(words):
    tf = Counter(words)
    return {w: (c / len(words)) * idf.get(w, 0) for w, c in tf.items()}

doc_vec = {d: tfidf(ws) for d, ws in tok.items()}

def cosine(a, b):
    dot = sum(a[w] * b.get(w, 0) for w in a)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

query = "natural language models"
q = tfidf(tokens(query))
print("Query:", query)
print("IDF of query terms:", {w: round(idf[w], 3) for w in tokens(query) if w in idf})
print("\nRank  Doc   Score   Text")
ranked = sorted(doc_vec, key=lambda d: cosine(q, doc_vec[d]), reverse=True)
for r, d in enumerate(ranked, 1):
    print(f"{r:>3}   {d}   {cosine(q, doc_vec[d]):.4f}  {docs[d][:48]}")
