# Finite-state machine that generates the plural form of English nouns.
# States: START -> (checks last letters) -> one of the plural-ending states
vowels = "aeiou"
irregular = {"child": "children", "man": "men", "woman": "women", "mouse": "mice",
             "foot": "feet", "tooth": "teeth", "person": "people"}

def pluralize(noun):
    state = "START"
    if noun in irregular:
        state = "IRREGULAR"
    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        state = "ADD_ES"
    elif noun.endswith("y") and len(noun) > 1 and noun[-2] not in vowels:
        state = "Y_TO_IES"
    elif noun.endswith("f"):
        state = "F_TO_VES"
    elif noun.endswith("fe"):
        state = "FE_TO_VES"
    else:
        state = "ADD_S"

    if state == "IRREGULAR":  return irregular[noun], state
    if state == "ADD_ES":     return noun + "es", state
    if state == "Y_TO_IES":   return noun[:-1] + "ies", state
    if state == "F_TO_VES":   return noun[:-1] + "ves", state
    if state == "FE_TO_VES":  return noun[:-2] + "ves", state
    return noun + "s", state

print(f"{'Noun':10s}{'Plural':12s}Final state")
for n in ["cat", "bus", "box", "church", "dish", "city", "boy", "wolf", "knife", "child", "mouse"]:
    p, st = pluralize(n)
    print(f"{n:10s}{p:12s}{st}")
