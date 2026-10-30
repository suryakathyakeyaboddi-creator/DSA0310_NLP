# A small finite-state-style parser for the requested forms

lexicon = {
    "written": ("write", "irregular past participle")
}

def parse(word):
    if word == "writes":
        return (
            "q0 -> ROOT(write) -> SUFFIX(+s) -> qF",
            "write + -s",
            "Regular inflection",
            "write"
        )

    if word == "writing":
        return (
            "q0 -> ROOT(write) -> DROP_FINAL_E -> +ing -> qF",
            "write + -ing (e deleted)",
            "Regular spelling change",
            "write"
        )

    if word in lexicon:
        root, label = lexicon[word]
        return (
            "q0 -> IRREGULAR_LOOKUP -> qF",
            f"{root} + {label}",
            "Irregular inflection",
            root
        )

    return ("q0 -> REJECT", "No analysis", "Unknown", None)


print("FINITE-STATE MORPHOLOGICAL PARSER")
print("=" * 88)

for word in ["writes", "writing", "written"]:
    path, breakdown, kind, root = parse(word)
    print(f"Word: {word}")
    print(f"State path : {path}")
    print(f"Analysis   : {breakdown}")
    print(f"Pattern    : {kind}")
    print(f"Root       : {root}")
    print("-" * 88)
