from transformers import pipeline

print("MULTILINGUAL CUSTOMER COMMUNICATION SYSTEM")

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

while True:
    text = input("\nEnter English sentence (or type 'exit'): ")

    if text.lower() == "exit":
        break

    result = translator(text)

    print("English:", text)
    print("French:", result[0]["translation_text"])
