from collections import Counter

print("SMART TEXT PREDICTION SYSTEM")

corpus = input("Enter training corpus: ").lower()
words = corpus.split()
bigrams = list(zip(words, words[1:]))
freq = Counter(bigrams)

print("\nBigram Frequency Table:")
for bigram, count in freq.items():
    print(bigram, ":", count)

start = input("\nEnter starting word: ").lower()
options = [(b[1], count) for b, count in freq.items() if b[0] == start]

if options:
    print("Possible next words:", dict(options))
    sequence = [start]
    current = start

    for _ in range(5):
        choices = [(b[1], count) for b, count in freq.items()
                   if b[0] == current]
        if not choices:
            break
        current = max(choices, key=lambda item: item[1])[0]
        sequence.append(current)

    print("Generated sequence:", " ".join(sequence))
else:
    print("No prediction available.")
