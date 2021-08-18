import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pickle
import pandas as pd

import os
workpath = os.path.dirname(os.path.abspath(__file__))

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
    top_10_indexes = list(score_series.iloc[1:11].index)
    for i in top_10_indexes:
        recommendation_feed.append(list(feed.index)[i])
    # print(recommendation_feed)
    return recommendation_feed

recommendation('Бежавший президент Афганистана рассказал о заговоре против него')

