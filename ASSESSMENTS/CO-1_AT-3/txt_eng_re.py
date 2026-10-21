
import re

# Sample text
text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""

def search_pattern(pattern):
    matches = re.findall(pattern, text, re.IGNORECASE)
    if matches:
        print("Matching patterns:", matches)
    else:
        print("No matching patterns found.")

while True:
    print("\n--- Text Search Engine ---")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        search_pattern(r'\b\d{2}/\d{2}/\d{4}\b')

    elif choice == '2':
        search_pattern(r'\b[6-9]\d{9}\b')

    elif choice == '3':
        search_pattern(r'#[A-Za-z0-9_]+')

    elif choice == '4':
        search_pattern(r'@[A-Za-z0-9_]+')

    elif choice == '5':
        prefix = input("Enter prefix: ")
        pattern = r'\b' + re.escape(prefix) + r'\w*'
        search_pattern(pattern)

    elif choice == '6':
        suffix = input("Enter suffix: ")
        pattern = r'\b\w*' + re.escape(suffix) + r'\b'
        search_pattern(pattern)

    elif choice == '7':
        word = input("Enter word to search: ")
        pattern = r'\b' + re.escape(word) + r'\b'
        search_pattern(pattern)

    elif choice == '8':
        print("Exiting search engine.")
        break

    else:
        print("Invalid choice. Please try again.")
