from rest_framework import viewsets
from urllib import request
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleSerializer
from ..models import Article

from mainapp.recommendations.test import recommendation




class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        if 'article-test-cookie-id' not in request.COOKIES:
            articles = Article.objects.all()
        if 'article-test-cookie-id' in request.COOKIES:
            info = str(request.COOKIES['article-test-cookie-id'])
            get_article = Article.objects.get(pk=info)
            rec = recommendation(get_article.title)

            articles = Article.objects.filter(title__in=rec).distinct('title')

        # rec = recommendation('В Mozilla испугались, что новый Firefox «сломает» сайты, и призвали на помощь пользователей')
        # articles = Article.objects.all()[:10]
        serializer = ArticleSerializer(articles, many=True)
        return Response({"data": serializer.data})




