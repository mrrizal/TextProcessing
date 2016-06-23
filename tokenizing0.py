from nltk.corpus import webtext
import nltk.data

para = webtext.raw('overheard.txt')

#load punktsentence tokenizer if you going tokenizing a lot of sentence
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
print(len(tokenizer.tokenize(para)))

tokenizer = nltk.data.load('tokenizers/punkt/PY3/webtext.pickle')
print(len(tokenizer.tokenize(para)))
