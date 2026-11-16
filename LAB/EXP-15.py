import nltk

pcfg = nltk.PCFG.fromstring("""
S   -> NP VP        [1.0]
NP  -> Det N        [0.5]
NP  -> NP PP        [0.2]
NP  -> 'John'       [0.3]
VP  -> V NP         [0.6]
VP  -> VP PP        [0.4]
PP  -> P NP         [1.0]
Det -> 'the'        [0.7]
Det -> 'a'          [0.3]
N   -> 'man'        [0.4]
N   -> 'telescope'  [0.3]
N   -> 'hill'       [0.3]
V   -> 'saw'        [1.0]
P   -> 'with'       [0.6]
P   -> 'on'         [0.4]
""")

sentence = "John saw the man with the telescope".split()
parser = nltk.ViterbiParser(pcfg)

print("Sentence:", " ".join(sentence))
for tree in parser.parse(sentence):
    print("\nMost probable parse (Viterbi):")
    print(tree)
    tree.pretty_print()
    print("Probability of the parse =", tree.prob())
