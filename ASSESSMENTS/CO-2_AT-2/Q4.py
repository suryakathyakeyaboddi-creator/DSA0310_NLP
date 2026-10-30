from dataclasses import dataclass
@dataclass
class Parse:
    word: str; prefix: str; base: str; suffix: str; derivational_path: str; word_class: str; meaning: str; normalized: str
RULES = {
"activate": Parse("activate","","act","-ivate","act -> activate","verb","cause to become active","ACTIVATE"),
"activation": Parse("activation","","act","-ivate + -ion (spelling adjustment)","act -> activate -> activation","noun","process or state of activating","ACTIVATE"),
"reactivation": Parse("reactivation","re-","act","-ivate + -ion","act -> activate -> activation -> reactivation","noun","activation again","ACTIVATE")}
def parse(word):
    word = word.lower().strip()
    if word not in RULES: raise ValueError(f"No rule defined for {word!r}")
    return RULES[word]
print("Q4 - LAYERED DERIVATIONAL MORPHOLOGICAL PARSING")
print("=" * 125)
print(f"{'WORD':<14}{'PREFIX':<8}{'BASE':<6}{'SUFFIX/CHANGE':<38}{'WORD CLASS':<12}{'INDEX KEY':<12}PATH")
print("-" * 125)
for word in ("activate","activation","reactivation"):
    p = parse(word)
    print(f"{p.word:<14}{p.prefix or '-':<8}{p.base:<6}{p.suffix:<38}{p.word_class:<12}{p.normalized:<12}{p.derivational_path}")
    print(f"  Meaning: {p.meaning}")
print("=" * 125)
