from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def article_detail(request, id):
    return render(request, 'index.html', {})
