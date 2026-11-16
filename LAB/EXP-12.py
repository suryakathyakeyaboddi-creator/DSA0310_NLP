import nltk

grammar_rules = [
    ("S",   ["NP", "VP"]),
    ("NP",  ["Det", "N"]), ("NP", ["NP", "PP"]), ("NP", ["PN"]),
    ("VP",  ["V", "NP"]),  ("VP", ["VP", "PP"]),
    ("PP",  ["P", "NP"]),
    ("Det", ["the"]), ("Det", ["a"]),
    ("N",   ["man"]), ("N", ["telescope"]), ("N", ["hill"]),
    ("PN",  ["John"]),
    ("V",   ["saw"]),
    ("P",   ["with"]), ("P", ["on"]),
]
nonterminals = {lhs for lhs, _ in grammar_rules}

def earley(words):
    chart = [[] for _ in range(len(words) + 1)]
    def add(i, state):
        if state not in chart[i]:
            chart[i].append(state)
    add(0, ("GAMMA", ("S",), 0, 0))                       # (lhs, rhs, dot, origin)
    for i in range(len(words) + 1):
        for lhs, rhs, dot, org in chart[i]:               # chart[i] may grow while iterating
            if dot < len(rhs):
                nxt = rhs[dot]
                if nxt in nonterminals:                   # PREDICTOR
                    for l, r in grammar_rules:
                        if l == nxt:
                            add(i, (l, tuple(r), 0, i))
                elif i < len(words) and words[i] == nxt:  # SCANNER
                    add(i + 1, (lhs, rhs, dot + 1, org))
            else:                                         # COMPLETER
                for l2, r2, d2, o2 in list(chart[org]):
                    if d2 < len(r2) and r2[d2] == lhs:
                        add(i, (l2, r2, d2 + 1, o2))
    return chart

def fmt(s):
    lhs, rhs, dot, org = s
    r = list(rhs); r.insert(dot, "•")
    return f"{lhs} -> {' '.join(r)} [{org}]"

sentence = "John saw a man"
words = sentence.split()
chart = earley(words)
print("Sentence:", sentence)
for i, states in enumerate(chart):
    print(f"\nChart[{i}]  ({len(states)} states)")
    for s in states[:5]:
        print("   ", fmt(s))
    if len(states) > 5:
        print("    ...")
accepted = any(s == ("GAMMA", ("S",), 1, 0) for s in chart[-1])
print("\nSentence accepted by Earley parser:", accepted)

# the same grammar using NLTK's Earley chart parser to build the parse tree
rules = "\n".join(l + " -> " + " ".join(x if x in nonterminals else "'" + x + "'" for x in r)
                  for l, r in grammar_rules)
parser = nltk.parse.EarleyChartParser(nltk.CFG.fromstring(rules))
for tree in parser.parse(words):
    print()
    print(tree)
