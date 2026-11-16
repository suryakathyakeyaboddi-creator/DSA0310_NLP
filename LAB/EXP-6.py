import random
from collections import defaultdict, Counter

corpus = ("the cat sat on the mat . the dog sat on the log . "
          "the cat chased the dog . the dog chased the cat . "
          "a cat and a dog sat on the mat .")
tokens = corpus.split()

# build bigram model: P(w2 | w1) from counts
bigrams = defaultdict(Counter)
for w1, w2 in zip(tokens, tokens[1:]):
    bigrams[w1][w2] += 1

print("Bigram probabilities for 'the':")
total = sum(bigrams["the"].values())
for w, c in bigrams["the"].most_common():
    print(f"  P({w} | the) = {c}/{total} = {c/total:.2f}")

def generate(start, length=10):
    word, out = start, [start]
    for _ in range(length - 1):
        nxt = bigrams[word]
        if not nxt:
            break
        word = random.choices(list(nxt), weights=nxt.values())[0]
        out.append(word)
    return " ".join(out)

random.seed(4)
print("\nGenerated text:")
for _ in range(4):
    print(" ", generate("the"))
