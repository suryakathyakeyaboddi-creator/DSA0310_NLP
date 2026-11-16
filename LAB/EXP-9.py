import re
import nltk

# rule-based tagger: (regular expression, tag), first match wins
patterns = [
    (r"(?i).*ing$", "VBG"),                  # gerunds
    (r".*ed$", "VBD"),                   # past tense
    (r".*(ch|sh|ss|x)es$", "VBZ"),       # 3rd person singular present
    (r".*ould$", "MD"),                  # modals
    (r".*'s$", "NN$"),                   # possessive nouns
    (r".*s$", "NNS"),                    # plural nouns
    (r"^-?[0-9]+(\.[0-9]+)?$", "CD"),    # cardinal numbers
    (r"(?i)^(the|a|an)$", "DT"),         # determiners
    (r"(?i)^(he|she|it|they|we|i|you)$", "PRP"),   # pronouns
    (r"(?i)^(and|or|but)$", "CC"),       # conjunctions
    (r"(?i)^(was|were|is|are)$", "VBD"), # forms of be
    (r".*ly$", "RB"),                    # adverbs
    (r".*", "NN"),                       # default: noun
]

def regex_tag(sentence):
    return [(w, next(t for p, t in patterns if re.match(p, w)))
            for w in sentence.split()]

for s in ["The dogs were running quickly", "She walked 3 miles and watches birds",
          "John's car could stop"]:
    print(regex_tag(s))

# the same idea using NLTK's built-in RegexpTagger
tagger = nltk.RegexpTagger(patterns)
print("\nNLTK RegexpTagger:", tagger.tag("The children played happily".split()))
