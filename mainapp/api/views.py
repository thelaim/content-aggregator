from rest_framework import viewsets
from urllib import request
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleSerializer
from ..models import Article




class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        if 'article' not in request.session:
            articles = Article.objects.all()
        if 'article' in request.session:
            info = str(request.session['article'][-1])
            articles = Article.objects.filter(id=info)
        serializer = ArticleSerializer(articles, many=True)
        return Response({"data": serializer.data})




