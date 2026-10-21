# DFA Simulator

# Accept DFA description
states = input("Enter states (space-separated): ").split()
alphabet = input("Enter input alphabet (space-separated): ").split()
initial_state = input("Enter initial state: ")
final_states = input("Enter final states (space-separated): ").split()

# Accept transition table
transitions = {}

print("Enter transitions:")
for state in states:
    for symbol in alphabet:
        next_state = input(f"Delta({state}, {symbol}) = ")
        transitions[(state, symbol)] = next_state

# Accept multiple input strings
n = int(input("Enter number of input strings: "))

for i in range(n):
    string = input(f"Enter string {i + 1}: ")

    current_state = initial_state
    path = [current_state]
    valid = True

    for symbol in string:
        if symbol not in alphabet:
            valid = False
            break

        current_state = transitions.get((current_state, symbol))

        if current_state is None:
            valid = False
            break

        path.append(current_state)

    print("Transition Path:")
    print(" -> ".join(path))

    if valid and current_state in final_states:
        print("Accepted")
    else:
        print("Rejected")
