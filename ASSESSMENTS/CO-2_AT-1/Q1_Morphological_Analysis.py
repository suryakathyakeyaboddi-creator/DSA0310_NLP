words = ["connected", "connecting", "connection"]

rules = {
    "connected": ("connect", "-ed", "Inflectional", "connect"),
    "connecting": ("connect", "-ing", "Inflectional", "connect"),
    "connection": ("connect", "-ion", "Derivational", "connect")
}

print("MORPHOLOGICAL ANALYSIS PIPELINE")
print("-" * 78)
print(f"{'Word':<14}{'Root':<12}{'Affix':<10}{'Type':<18}{'Normalized'}")
print("-" * 78)

for word in words:
    root, affix, kind, normalized = rules[word]
    print(f"{word:<14}{root:<12}{affix:<10}{kind:<18}{normalized}")

print("-" * 78)
