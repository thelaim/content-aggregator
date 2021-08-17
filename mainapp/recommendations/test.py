import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pickle
import pandas as pd

import os
workpath = os.path.dirname(os.path.abspath(__file__))

import time
# start_time = time.time()
def recommendation(feed_name):
    opencsv = open(os.path.join(workpath, "data.csv"), "rb")
    feed = pd.read_csv(opencsv, delimiter=',', error_bad_lines=False)
    feed.set_index('title', inplace=True)
    print(1)
    openmatrix = open(os.path.join(workpath, "tfidf_matrix.pickle"), "rb")
    cos_sim = pickle.load(openmatrix)
    # cos_sim = pickle.load(open("recommendations/tfidf_matrix.pickle", "rb"))

    name = pd.Series(feed.index)

    recommendation_feed = []
    idx = name[name == feed_name].index[0]
    score_series = pd.Series(cos_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[1:101].index)
    for i in top_10_indexes:
        recommendation_feed.append(list(feed.index)[i])
    return recommendation_feed

recommendation('В Mozilla испугались, что новый Firefox «сломает» сайты, и призвали на помощь пользователей')

# cosine_sim =  joblib.load("tfidf_matrix.joblib")
# print(2)
#
#
# # print(tfidf_matrix)
# # #Output the shape of tfidf_matrix
# # print(tfidf_matrix.shape)
# # # print(tfidf.get_feature_names()[5000:5010])
# # cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# # print(cosine_sim.shape)
# indices = pd.Series(metadata.index, index=metadata['title']).drop_duplicates()
# print(3)
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