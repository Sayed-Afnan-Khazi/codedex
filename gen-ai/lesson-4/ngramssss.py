import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
nltk.download('punkt_tab')

text = "Hello world! I'm excited to learn about LLMs!"
tokens = word_tokenize(text)
print("Tokens",tokens)
n = 2
ngms = list(ngrams(tokens, n))
print("Ngrams:",ngms)
print(len(ngms) == len(tokens)-n+1)