from django.contrib.auth import authenticate

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer, UserSerializer


class LoginView(APIView):
    """
    Allow admin user to login
    """

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = authenticate(username=request.data["username"],
                                password=request.data["password"])
            if user is not None:
                return Response(serializer.data,
                                status=status.HTTP_200_CREATED)
            else:
                return Response({"error": "Invalid username or password."},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
