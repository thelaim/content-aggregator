import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import linear_kernel

feed = pd.read_csv('data.csv', delimiter=',', error_bad_lines=False)
feed.set_index('title', inplace=True)
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(feed['description'].values.astype('U'))


cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

pickle.dump(cos_sim, open("tfidf_matrix.pickle", "wb"))


