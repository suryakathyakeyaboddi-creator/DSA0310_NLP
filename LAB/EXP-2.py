# DFA that accepts strings over {a, b} ending with 'ab'
# States: q0 (start), q1 (last symbol 'a'), q2 (last two symbols 'ab', accepting)
transitions = {
    ("q0", "a"): "q1", ("q0", "b"): "q0",
    ("q1", "a"): "q1", ("q1", "b"): "q2",
    ("q2", "a"): "q1", ("q2", "b"): "q0",
}
start, accepting = "q0", {"q2"}

def accepts(s):
    state = start
    for ch in s:
        if (state, ch) not in transitions:
            return False
        state = transitions[(state, ch)]
    return state in accepting

for s in ["ab", "aab", "abab", "bbab", "aba", "abb", "b", "a", "ba", "aaab"]:
    print(f"{s:6s} -> {'Accepted' if accepts(s) else 'Rejected'}")
