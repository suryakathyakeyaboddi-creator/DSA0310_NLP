# Simple top-down (recursive descent) parser with backtracking for a CFG
grammar = {
    "S":   [["NP", "VP"]],
    "NP":  [["Det", "N"], ["Det", "Adj", "N"], ["PN"]],
    "VP":  [["V", "NP"], ["V"], ["VP", "PP"]],
    "PP":  [["P", "NP"]],
    "Det": [["the"], ["a"]],
    "N":   [["dog"], ["cat"], ["park"], ["man"]],
    "Adj": [["big"], ["small"]],
    "PN":  [["John"], ["Mary"]],
    "V":   [["saw"], ["chased"], ["slept"]],
    "P":   [["in"], ["with"]],
}

def parse(symbol, words, pos, depth=0):
    """Yield (tree, new_position) for every way `symbol` can derive words[pos:...]"""
    if symbol not in grammar:                       # terminal
        if pos < len(words) and words[pos] == symbol:
            yield symbol, pos + 1
        return
    for rule in grammar[symbol]:                    # try each production top-down
        if rule[0] == symbol:                       # avoid left recursion (VP -> VP PP)
            continue
        yield from expand(symbol, rule, words, pos)

def expand(symbol, rule, words, pos, children=None):
    children = children or []
    if len(children) == len(rule):
        yield (symbol, children), pos
        return
    for tree, p in parse(rule[len(children)], words, pos):
        yield from expand(symbol, rule, words, p, children + [tree])

def show(tree):
    if isinstance(tree, str):
        return tree
    return "(" + tree[0] + " " + " ".join(show(c) for c in tree[1]) + ")"

for sentence in ["the dog chased a cat", "John saw the big man", "Mary slept",
                 "the dog the cat chased"]:
    words = sentence.split()
    results = [t for t, p in parse("S", words, 0) if p == len(words)]
    print(f"'{sentence}'")
    print("   ", show(results[0]) if results else "NOT in the language")
