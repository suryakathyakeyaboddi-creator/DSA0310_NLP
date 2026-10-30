words = ["played", "player", "playing"]

rules = {
    "played": ("play", "-ed", "Inflectional", "play"),
    "player": ("play", "-er", "Derivational (agent noun)", "play"),
    "playing": ("play", "-ing", "Inflectional", "play")
}

print("STEMMING-BASED SEARCH PREPROCESSING")
print("-" * 82)
print(f"{'Word':<13}{'Stem':<10}{'Affix':<10}{'Transformation':<29}{'Normalized'}")
print("-" * 82)

for word in words:
    stem, affix, kind, normalized = rules[word]
    print(f"{word:<13}{stem:<10}{affix:<10}{kind:<29}{normalized}")

print("-" * 82)
