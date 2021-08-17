from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

import sys
sys.path.insert(1, 'recommendations')
from mainapp.recommendations.test import recommendation

import os
workpath = os.path.dirname(os.path.abspath(__file__))

import pickle
import pandas as pd

def index(request):
    return render(request, 'index.html', {})

def article_detail(request, id):
    return render(request, 'index.html', {})

@login_required
def parse_data(request):
    return redirect('/')

def parse_data(request):
    # feed_name = 'В Mozilla испугались, что новый Firefox «сломает» сайты, и призвали на помощь пользователей'
    # opencsv = open(os.path.join(workpath, "recommendations/data.csv"), "rb")
    # feed = pd.read_csv(opencsv, delimiter=',', error_bad_lines=False)
    # feed.set_index('title', inplace=True)
    # print(1)
    # openmatrix = open(os.path.join(workpath, "recommendations/tfidf_matrix.pickle"), "rb")
    # cos_sim = pickle.load(openmatrix)
    # # cos_sim = pickle.load(open("recommendations/tfidf_matrix.pickle", "rb"))
    #
    # name = pd.Series(feed.index)
    #
    # recommendation_feed = []
    # idx = name[name == feed_name].index[0]
    # score_series = pd.Series(cos_sim[idx]).sort_values(ascending=False)
    # top_10_indexes = list(score_series.iloc[1:101].index)
    # for i in top_10_indexes:
    #     recommendation_feed.append(list(feed.index)[i])
    info = recommendation('В Mozilla испугались, что новый Firefox «сломает» сайты, и призвали на помощь пользователей')
    return HttpResponse("Welcome Guest." + str(info))

def setcookie(request, pk):
    if 'article' not in request.session:
        request.session['article'] = []
        request.session['article'].append(pk)
        request.session.modified = True
        return redirect('/')
    elif pk != request.session['article'][-1]:
        request.session['article'].append(pk)
        request.session.modified = True
        return redirect('/')
    else:
        return redirect('/')
    # response = HttpResponse("Welcome Guest.")
    # response.set_cookie('article', 1)

def get_cookie(request):
    info = str(request.COOKIES['article-test-cookie-id'][-1])
    return HttpResponse("Welcome Guest." + info)

def delcookie(request):
    if 'article' not in request.session:
        return redirect('/')
    if 'article' in request.session:
        del request.session['article']
        request.session.modified = True
        return redirect('/')


