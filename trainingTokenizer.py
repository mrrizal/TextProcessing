from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext


#custom tokenizer with training using nltk
text = webtext.raw('overheard.txt')
sent_tokenizer = PunktSentenceTokenizer(text)
sents1 = sent_tokenizer.tokenize(text)
print(sents1[0])
print(sents1[678])
print(len(sents1))

#default tokenizer
from nltk.tokenize import sent_tokenize
sents2 = sent_tokenize(text)
print(sents2[0])
print(sents2[678])
print(len(sents2))

