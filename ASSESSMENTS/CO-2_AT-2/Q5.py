from dataclasses import dataclass
@dataclass
class Inflection:
    word: str; suffix: str; grammar: str; root: str; normalized: str
# The lexicon makes the e-restoration in creating explicit.
RULES = {
"create": Inflection("create","","base form","create","CREATE"),
"creates": Inflection("creates","-s","third-person singular present","create","CREATE"),
"creating": Inflection("creating","-ing","present participle / progressive","create","CREATE")}
def normalize(word):
    word = word.lower().strip()
    if word not in RULES: raise ValueError(f"No inflection rule defined for {word!r}")
    return RULES[word]
print("Q5 - INFLECTIONAL NORMALIZATION FOR SEARCH")
print("=" * 86)
print(f"{'WORD':<12}{'SUFFIX':<8}{'GRAMMATICAL FORM':<36}{'ROOT':<10}{'NORMALIZED':<12}")
print("-" * 86)
for word in ("create","creates","creating"):
    p = normalize(word)
    print(f"{p.word:<12}{p.suffix or '-':<8}{p.grammar:<36}{p.root:<10}{p.normalized:<12}")
print("=" * 86)
