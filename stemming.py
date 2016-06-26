from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer, SnowballStemmer

stemmer = PorterStemmer()
print(stemmer.stem("watching"))
print(stemmer.stem("cookery"))

#menggunakan LancasterStemmer
stemmer = LancasterStemmer()
print(stemmer.stem("watching"))
print(stemmer.stem("cookery"))

#menggunakan regex, digunakan hanya pada kasus" tertentu
stemmer = RegexpStemmer('ing')
print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))

print(SnowballStemmer.languages)
spannish_stemmer = SnowballStemmer('spanish')
print(spannish_stemmer.stem('hola'))
