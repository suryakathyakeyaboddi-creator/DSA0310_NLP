# Transformation-based (Brill style) tagging:
# 1) start with the most frequent tag for every word (baseline)
# 2) apply transformation rules:  change tag A to B if the previous tag is C
lexicon = {"the": "DT", "a": "DT", "dog": "NN", "can": "MD", "run": "VB",
           "fish": "NN", "to": "TO", "I": "PRP", "want": "VB", "race": "NN"}

# (from_tag, to_tag, condition on previous tag)
rules = [
    ("NN", "VB", "TO"),   # NN -> VB if previous tag is TO       ("to race")
    ("NN", "VB", "MD"),   # NN -> VB if previous tag is MD       ("can fish")
    ("VB", "NN", "DT"),   # VB -> NN if previous tag is DT       ("the run")
]

def tag(sentence):
    words = sentence.split()
    tags = [lexicon.get(w, "NN") for w in words]
    print("Initial   :", list(zip(words, tags)))
    for frm, to, prev in rules:
        for i in range(1, len(tags)):
            if tags[i] == frm and tags[i - 1] == prev:
                print(f"  rule [{frm}->{to} after {prev}] fires on '{words[i]}'")
                tags[i] = to
    print("Final     :", list(zip(words, tags)))

tag("I want to race")
print()
tag("the dog can fish")
print()
tag("a run")
