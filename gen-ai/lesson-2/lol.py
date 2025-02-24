import nltk
nltk.download('punkt_tab')

text = "Hey y'all my name is Afnan and I like cool tech."

tokens  = nltk.word_tokenize(text.lower())

print(tokens)
