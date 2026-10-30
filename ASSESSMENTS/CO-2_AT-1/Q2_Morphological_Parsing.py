words = ["unhappy", "happiness", "happily"]

analysis = {
    "unhappy": ("un-", "happy", "—", "Derivational (negation)", "happy"),
    "happiness": ("—", "happy (happi-)", "-ness", "Derivational (noun)", "happy"),
    "happily": ("—", "happy (happi-)", "-ly", "Derivational (adverb)", "happy")
}

print("MORPHOLOGICAL PARSING FOR SENTIMENT ANALYSIS")
print("-" * 100)
print(f"{'Word':<13}{'Prefix':<9}{'Base':<19}{'Suffix':<10}{'Type':<28}{'Root'}")
print("-" * 100)

for word in words:
    prefix, base, suffix, kind, root = analysis[word]
    print(f"{word:<13}{prefix:<9}{base:<19}{suffix:<10}{kind:<28}{root}")

print("-" * 100)
