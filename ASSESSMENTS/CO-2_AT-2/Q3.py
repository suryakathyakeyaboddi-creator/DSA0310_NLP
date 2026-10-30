from dataclasses import dataclass
@dataclass
class Morphology:
    word: str; root: str; suffix: str; derivation: str; level: int; normalized: str; meaning: str
RULES = {
"govern": Morphology("govern","govern","","root/base",0,"GOVERN","to direct or control"),
"government": Morphology("government","govern","-ment","govern + -ment",1,"GOVERN","governing authority or system"),
"governance": Morphology("governance","govern","-ance","govern + -ance",1,"GOVERN","process or manner of governing")}
def normalize(word):
    word = word.lower().strip()
    if word not in RULES: raise ValueError(f"No morphology rule defined for {word!r}")
    return RULES[word]
print("Q3 - MORPHOLOGY-BASED NORMALIZATION")
print("=" * 112)
print(f"{'WORD':<12}{'ROOT':<10}{'SUFFIX':<8}{'DERIVATION':<20}{'LEVEL':<8}{'INDEX KEY':<12}MEANING")
print("-" * 112)
for word in ("govern","government","governance"):
    p = normalize(word)
    print(f"{p.word:<12}{p.root:<10}{p.suffix or '-':<8}{p.derivation:<20}{p.level:<8}{p.normalized:<12}{p.meaning}")
print("=" * 112)
