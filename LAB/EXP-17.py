import nltk
from nltk.corpus import wordnet as wn

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

word = "bank"
syns = wn.synsets(word)
print(f"'{word}' has {len(syns)} synsets. First four:\n")
for s in syns[:4]:
    print(f"{s.name()}  ({s.pos()})")
    print(f"    meaning : {s.definition()}")
    print(f"    lemmas  : {s.lemma_names()[:4]}")
    if s.examples():
        print(f"    example : {s.examples()[0]}")

dog = wn.synset("dog.n.01")
print("\ndog.n.01 hypernyms :", [h.name() for h in dog.hypernyms()])
print("dog.n.01 hyponyms  :", [h.name() for h in dog.hyponyms()][:4])

good = wn.synset("good.a.01")
print("\nantonym of 'good'  :", good.lemmas()[0].antonyms()[0].name())
print("synonyms of 'happy':", sorted({l.name() for s in wn.synsets("happy") for l in s.lemmas()})[:6])

cat = wn.synset("cat.n.01")
print("\nsimilarity(dog, cat)   =", round(dog.path_similarity(cat), 3))
print("similarity(dog, table) =", round(dog.path_similarity(wn.synset("table.n.01")), 3))
