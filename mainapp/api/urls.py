from django.urls import path

from rest_framework import routers
from .views import ArticleViewSet, ArticleView

router = routers.SimpleRouter()
router.register('article', ArticleViewSet, basename='article')

# urlpatterns = []
urlpatterns = [
    path('article-test/', ArticleView.as_view()),
]
urlpatterns += router.urls



