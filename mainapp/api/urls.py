from django.urls import path

from rest_framework import routers
from .views import ArticleViewSet

router = routers.SimpleRouter()
router.register('Article', ArticleViewSet, basename='Article')

urlpatterns = []
urlpatterns += router.urls