import re

text = "Contact us at support@example.com or sales@shop.in. Call 044-2345-6789 on 12/05/2024."

# re.search - first match of a pattern
m = re.search(r"\d{2}/\d{2}/\d{4}", text)
print("Date found      :", m.group() if m else None)

# re.findall - all matches
print("Emails found    :", re.findall(r"[\w.]+@[\w.]+\.\w+", text))
print("Phone numbers   :", re.findall(r"\d{3}-\d{4}-\d{4}", text))

# re.match - match only at the beginning of the string
print("Starts with 'Contact':", bool(re.match(r"Contact", text)))

# re.sub - replace a pattern
print("Masked text     :", re.sub(r"\d", "#", text))

# re.split - split on punctuation / spaces
print("Words           :", re.split(r"[ .,]+", text)[:6])
