from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from .models import Article

import sys
sys.path.insert(1, 'recommendations')
from mainapp.recommendations.test import recommendation
from mainapp.parsing.pars import Parser

import os
workpath = os.path.dirname(os.path.abspath(__file__))


def index(request):
    return render(request, 'index.html', {})

def article_detail(request, id):
    return render(request, 'index.html', {})



def parse_data(request):          # здесь мы достаем данные из парсера и сохраняем
    data = Parser()
    data_save_lenta = data.data_lenta('https://lenta.ru/rss/news')
    data_save_cnews = data.data_cnews('https://www.cnews.ru/inc/rss/news.xml')
    for key, value in data_save_lenta.items():
        article = Article(title=key, content=value[1], url_article=value[0], url_photo=value[2])
        article.save()
    for key, value in data_save_cnews.items():
        article = Article(title=key, content=value[1], url_article=value[0])
        article.save()
    return HttpResponse("Welcome Guest.")

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

def get_cookie(request):
    info = request.COOKIES['article-test-cookie-id']
    return HttpResponse("Welcome Guest." + info)

def delcookie(request):
    if 'article-test-cookie-id' not in request.COOKIES:
        return redirect('/')
    if 'article-test-cookie-id' in request.COOKIES:
        del request.COOKIES['article-test-cookie-id']
        request.session.modified = True
        return redirect('/')


