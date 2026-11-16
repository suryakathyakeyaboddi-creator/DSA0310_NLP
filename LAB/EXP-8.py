from collections import defaultdict, Counter

# tiny tagged training corpus
train = [
    [("the", "DT"), ("dog", "NN"), ("barks", "VBZ")],
    [("the", "DT"), ("cat", "NN"), ("sleeps", "VBZ")],
    [("a", "DT"), ("dog", "NN"), ("runs", "VBZ")],
    [("the", "DT"), ("big", "JJ"), ("dog", "NN"), ("runs", "VBZ")],
    [("a", "DT"), ("small", "JJ"), ("cat", "NN"), ("sleeps", "VBZ")],
    [("dogs", "NNS"), ("bark", "VBP")],
    [("cats", "NNS"), ("sleep", "VBP")],
]

# most probable tag for each word: P(tag | word) = count(word, tag) / count(word)
counts = defaultdict(Counter)
tag_count = Counter()
for sent in train:
    for w, t in sent:
        counts[w][t] += 1
        tag_count[t] += 1
default_tag = "NN"          # unknown words are assumed to be nouns

def tag(sentence):
    return [(w, counts[w].most_common(1)[0][0] if w in counts else default_tag)
            for w in sentence.lower().split()]

print("P(tag | word) for some words:")
for w in ["dog", "runs", "the"]:
    tot = sum(counts[w].values())
    for t, c in counts[w].items():
        print(f"  P({t} | {w}) = {c}/{tot} = {c/tot:.2f}")

for s in ["the big cat runs", "a dog sleeps", "the zebra runs"]:
    print("\n", s, "->", tag(s))
