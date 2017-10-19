from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Article, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        max_length=None,
        min_length=None,
        allow_blank=False)

    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password'},
        required=True,
        write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
