from dataclasses import dataclass
@dataclass
class Analysis:
    word: str; prefix: str; root: str; suffix: str; category: str; meaning: str; normalized: str
RULES = {
"disagree": Analysis("disagree","dis-","agree","","derivational prefix","negation/opposition: not agree","AGREE"),
"agreement": Analysis("agreement","","agree","-ment","derivational suffix; noun","state, act, or result of agreeing","AGREE"),
"agreeable": Analysis("agreeable","","agree","-able","derivational suffix; adjective","pleasant or acceptable; capable of being agreed to","AGREE")}
def parse(word):
    word = word.lower().strip()
    if word not in RULES: raise ValueError(f"No rule defined for {word!r}")
    return RULES[word]
print("Q2 - MORPHOLOGICAL PARSING FOR SENTIMENT ANALYSIS")
print("=" * 135)
print(f"{'WORD':<12}{'PREFIX':<8}{'ROOT':<8}{'SUFFIX':<8}{'CATEGORY':<32}{'NORMALIZED':<12}MEANING")
print("-" * 135)
for word in ("disagree","agreement","agreeable"):
    p = parse(word)
    print(f"{p.word:<12}{p.prefix or '-':<8}{p.root:<8}{p.suffix or '-':<8}{p.category:<32}{p.normalized:<12}{p.meaning}")
print("=" * 135)
