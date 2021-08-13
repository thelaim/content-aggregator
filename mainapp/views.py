from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {})

def article_detail(request, id):
    return render(request, 'index.html', {})

def setcookie(request):
    if 'article' not in request.session:
        request.session['article'] = []
    if 2 not in request.session['article']:
        request.session['article'].append(2)
        request.session.modified = True
        return redirect('/')
    # response = HttpResponse("Welcome Guest.")
    # response.set_cookie('article', 1)

def get_cookie(request):
    info = str(request.session['article'][-1])
    return HttpResponse("Welcome Guest." + info)

def delcookie(request):
    if 'article' not in request.session:
        return redirect('/')
    if 'article' in request.session:
        del request.session['article']
        request.session.modified = True
        return redirect('/')


