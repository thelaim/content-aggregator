from django.urls import path

from rest_framework import routers
from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = []
urlpatterns += router.urls