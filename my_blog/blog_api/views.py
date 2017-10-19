from rest_framework import viewsets

from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Allow for CRUD functionality for a category resource
    Request methods (api/v1/categories): POST, GET
    Request methods (api/v1/categories/<id>): GET, PUT, DELETE
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Allow for CRUD functionality for a article resource
    Request methods (api/v1/articles): POST, GET
    Request methods (api/v1/articles/<id>): GET, PUT, DELETE
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
