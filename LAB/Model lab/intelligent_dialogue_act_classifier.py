print("INTELLIGENT DIALOGUE ACT CLASSIFIER")

messages = []
n = int(input("How many messages? "))

for i in range(n):
    messages.append(input(f"Enter message {i + 1}: ").strip())

print("\nClassification Results")
print("----------------------")

for message in messages:
    text = message.lower()

    if any(word in text for word in ["hello", "hi", "good morning", "good evening"]):
        category = "Greeting"
    elif any(word in text for word in ["please", "help", "could you", "would you"]):
        category = "Request"
    elif any(word in text for word in ["yes", "agree", "okay", "sure", "confirmed"]):
        category = "Confirmation"
    elif any(word in text for word in ["unhappy", "bad", "problem", "complaint", "not satisfied"]):
        category = "Complaint"
    elif "?" in text or text.startswith(("what", "why", "how", "when", "where", "who", "is", "are", "can", "do")):
        category = "Question"
    else:
        category = "Unknown"

    print(f"{message} : {category}")
