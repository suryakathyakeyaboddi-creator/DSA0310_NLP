import nltk
from nltk.grammar import FeatureGrammar
from nltk.parse import FeatureChartParser

# CFG with agreement features: NUM (sg / pl) must be the same on NP, VP, Det, N, V
fcfg = FeatureGrammar.fromstring("""
S -> NP[NUM=?n] VP[NUM=?n]
NP[NUM=?n] -> Det[NUM=?n] N[NUM=?n]
VP[NUM=?n] -> V[NUM=?n] | V[NUM=?n] NP[]
Det[NUM=sg] -> 'this' | 'the' | 'a'
Det[NUM=pl] -> 'these' | 'the'
N[NUM=sg] -> 'dog' | 'cat'
N[NUM=pl] -> 'dogs' | 'cats'
V[NUM=sg] -> 'barks' | 'sees'
V[NUM=pl] -> 'bark' | 'see'
""")
parser = FeatureChartParser(fcfg)

tests = ["the dog barks", "the dogs bark", "this dog sees the cat",
         "the dog bark", "the dogs barks", "these dog barks", "a cats see"]
for s in tests:
    ok = any(True for _ in parser.parse(s.split()))
    print(f"{s:25s} -> {'AGREEMENT OK' if ok else 'AGREEMENT ERROR'}")
