from dataclasses import dataclass
@dataclass
class Parse:
    word: str; root: str; prefix: str; suffix: str; form_type: str; normalized: str; note: str
WORDS = ["analyzing", "analysis", "analytical"]
LEXICON = {
"analyzing": Parse("analyzing","analyze","","-ing","inflectional (present participle)","ANALYZE","analyze + -ing; final e is dropped"),
"analysis": Parse("analysis","analysis","","lexical alternation","related lexical noun (irregular family form)","ANALYZE","not safely segmented by simple suffix stripping"),
"analytical": Parse("analytical","analysis","","-ical","derivational (adjective)","ANALYZE","adjective related to analysis")}
def analyze(word):
    word = word.lower().strip()
    if word not in LEXICON: raise ValueError(f"No morphology rule or lexical entry for: {word}")
    return LEXICON[word]
print("Q1 - RULE-BASED MORPHOLOGICAL ANALYSIS")
print("=" * 145)
print(f"{'WORD':<12}{'ROOT/BASE':<12}{'PREFIX':<8}{'SUFFIX/CHANGE':<22}{'TYPE':<46}{'INDEX KEY':<12}NOTE")
print("-" * 145)
for token in WORDS:
    p = analyze(token)
    print(f"{p.word:<12}{p.root:<12}{p.prefix or '-':<8}{p.suffix:<22}{p.form_type:<46}{p.normalized:<12}{p.note}")
print("=" * 145)
