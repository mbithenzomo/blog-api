# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Article, Category


class TestViews(APITestCase):
    """
    Test that API calls work as expected
    """

    def setUp(self):
        """
        Create a admin user using the model,
        and a category and an article
        using an API call before every test
        """

        self.admin = User(
            email="blog_admin@test.com",
            password="testpassword"
        )
        self.admin.save()

        self.category_data = {
            "name": "Technology"
        }
        self.response_category = self.client.post("/api/v1/categories/",
                                                  self.category_data,
                                                  format="json")

        self.article_data = {
            "writer": self.admin,
            "title": "Test Article 1",
            "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing \
                    elit. Aenean commodo ligula eget dolor. Aenean massa. \
                    Cum sociis natoque penatibus et magnis dis parturient \
                    montes, nascetur ridiculus mus. Donec quam felis, \
                    ultricies nec, pellentesque eu, pretium quis, sem. ",
            "category": str(self.response_category.data["id"]),
            "image": "http://testimage.com"
        }
        self.response_article = self.client.post("/api/v1/articles/",
                                                 self.artcile_data,
                                                 format="json")

    def test_create_category_using_api(self):

        new_category_data = {
            "name": "Technology"
        }

        response_category = self.client.post("/api/v1/categories/",
                                             new_category_data,
                                             format="json")
        self.assertEqual(response_category.status_code,
                         status.HTTP_201_CREATED)

        category_count = Category.objects.count()
        self.assertEqual(category_count, 2)

    def test_create_article_using_api(self):

        new_article_data = {
            "writer": self.admin,
            "title": "Test Article 2",
            "content": "Lorem ipsum dolor sit amet, consectetuer adipiscing \
                    elit. Aenean commodo ligula eget dolor. Aenean massa. \
                    Cum sociis natoque penatibus et magnis dis parturient \
                    montes, nascetur ridiculus mus. Donec quam felis, \
                    ultricies nec, pellentesque eu, pretium quis, sem. ",
            "category": str(self.response_category.data["id"]),
            "image": "http://testimage.com"
        }

        response_article = self.client.post("/api/v1/articles/",
                                            new_article_data,
                                            format="json")
        self.assertEqual(response_article.status_code,
                         status.HTTP_201_CREATED)

        article_count = Article.objects.count()
        self.assertEqual(article_count, 2)
