import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel

import time
# start_time = time.time()

# stopwords = set(stopwords.words('english'))
# print(1)
# #time.sleep(5)
# print(2)
feed = pd.read_csv('data.csv', delimiter=',', error_bad_lines=False)
feed.set_index('title', inplace=True)
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(feed['description'].values.astype('U'))

# print(tfidf_matrix)
# print(tfidf_matrix.shape)

# cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

pickle.dump(cos_sim, open("tfidf_matrix.pickle", "wb"))

# name = pd.Series(feed.index)
# def recommendation(feed_name, cos_sim = cos_sim):
#     recommendation_feed = []
#     idx = name[name == feed_name].index[0]
#     score_series = pd.Series(cos_sim[idx]).sort_values(ascending=False)
#     top_10_indexes = list(score_series.iloc[1:101].index)
#     for i in top_10_indexes:
#         recommendation_feed.append(list(feed.index)[i])
#     print("#"*30)
#     print("Новости похожие на эту: WhatsApp глючит на смартфонах Samsung. Как этого избежать")
#     print("Найденные схожие статьи и новости:")
#     for i in recommendation_feed:
#         print(i)
#
#     print("--- %s seconds ---" % (time.time() - start_time))
# recommendation('WhatsApp глючит на смартфонах Samsung. Как этого избежать')






# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics.pairwise import linear_kernel
#
# import pickle
# import joblib
# import time
# start_time = time.time()
#
# # Load Movies Metadata
# metadata = pd.read_csv('movies_metadata.csv', low_memory=False, encoding='latin-1', error_bad_lines=False)[:20000]
# # metadata = data.sample(20000)
#
# tfidf = TfidfVectorizer(stop_words='english')
# #Replace NaN with an empty string
# metadata['overview'] = metadata['overview'].fillna('')
# #overview
# #Construct the required TF-IDF matrix by fitting and transforming the data
# tfidf_matrix = tfidf.fit_transform(metadata['overview'])
#
#
# # pickle.dump(tfidf_matrix, open("tfidf_matrix.pickle", "wb"))
#
# print(tfidf_matrix)
# #Output the shape of tfidf_matrix
# print(tfidf_matrix.shape)
# print(tfidf.get_feature_names()[5000:5010])
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# # pickle.dump(cosine_sim, open("tfidf_matrix.pickle", "wb"))
# # joblib.dump(cosine_sim, "tfidf_matrix.joblib", compress=True)
# print(cosine_sim.shape)
# indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
#
# def get_recommendations(title, cosine_sim=cosine_sim):
#     # Get the index of the movie that matches the title
#     idx = indices[title]
#
#     # Get the pairwsie similarity scores of all movies with that movie
#     sim_scores = list(enumerate(cosine_sim[idx]))
#
#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#
#     # Get the scores of the 10 most similar movies
#     sim_scores = sim_scores[1:11]
#
#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]
#
#     # Return the top 10 most similar movies
#     # return metadata['title'].iloc[movie_indices]
#     print(metadata['title'].iloc[movie_indices])
#     print("--- %s seconds ---" % (time.time() - start_time))
#
# get_recommendations('Toy Story')

