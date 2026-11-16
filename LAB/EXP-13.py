import nltk

grammar = nltk.CFG.fromstring("""
S   -> NP VP
NP  -> Det N | Det Adj N | NP PP | PN
VP  -> V NP | VP PP
PP  -> P NP
Det -> 'the' | 'a'
Adj -> 'big' | 'old'
N   -> 'dog' | 'cat' | 'park' | 'bone'
PN  -> 'John'
V   -> 'saw' | 'chased' | 'buried'
P   -> 'in' | 'with'
""")

sentence = "John saw the big dog in the park".split()
parser = nltk.ChartParser(grammar)

trees = list(parser.parse(sentence))
print("Sentence:", " ".join(sentence))
print("Number of parse trees:", len(trees))
for i, tree in enumerate(trees, 1):
    print(f"\nParse tree {i}:")
    print(tree)
    tree.pretty_print()
