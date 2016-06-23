# import punkt
import nltk.tokenize.punkt

# Make a new Tokenizer
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

# Read in training corpus (one example: Slovene)
import codecs
text = codecs.open("/home/rizal/nltk_data/corpora/webtext/overheard.txt","Ur","ISO-8859-2").read()

# Train tokenizer
tokenizer.train(text)

# Dump pickled tokenizer
import pickle
out = open("webtext.pickle","wb")
pickle.dump(tokenizer, out)
