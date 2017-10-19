from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

# [WIP] Permissions
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer, UserSerializer


class LoginView(APIView):
    """
    Allow admin user to login
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=request.data["username"],
                                password=request.data["password"])
            if user is not None:
                login(request, user)
                return Response({"message": "successfully logged in!"},
                                status=status.HTTP_200_OK)
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
    # [WIP] Permissions
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Allow for CRUD functionality for a article resource
    Request methods (api/v1/articles): POST, GET
    Request methods (api/v1/articles/<id>): GET, PUT, DELETE
    """
    # [WIP] Permissions
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
