import sklearn
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pandas", lineno=570)

import numpy

example = ["Machine learning is super fun",
"python is super, super cool",
"statistics is cool, too",
"data science is fun",
"python is great for machine learning",
"i like football",
"football is great to watch"]

vectorize = CountVectorizer(min_df = 1, stop_words = 'english')
dtm = vectorize.fit_transform(example)

print(pd.DataFrame(dtm.toarray(), index=example, columns=vectorize.get_feature_names()).head(10))