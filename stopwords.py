from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

english_stop = set(stopwords.words('english'))

words = "can't is a contraction."

#tokeniziner
tokenizer = RegexpTokenizer('\s+', gaps=True)

#remove stopword
print([word for word in tokenizer.tokenize(words) if word not in english_stop])

print(stopwords.fileids())
