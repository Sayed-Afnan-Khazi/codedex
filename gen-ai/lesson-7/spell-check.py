from textblob import TextBlob

print("Welcome to Afnan's simple spell checker!")
text = input("Enter some text:")

blob = TextBlob(text)

corrected_text = blob.correct()
print(f"Spell check result: {corrected_text}")

