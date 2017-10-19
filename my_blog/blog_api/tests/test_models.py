# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Article, Category


class TestModels(TestCase):
    """
    Test that the models can be used to create
    resources that are saved in the database
    """

    def setUp(self):
        """
        Create an admin user, a category and
        an article before each test is run
        """

        self.admin = User(
            email="blog_admin@test.com",
            password="testpassword"
        )
        self.admin.save()

        self.first_category = Category(
            name="Technology"
        )
        self.first_category.save()

        self.first_article = Article(
            writer=self.admin,
            title="Test Article 1",
            content="Lorem ipsum dolor sit amet, consectetuer adipiscing \
                    elit. Aenean commodo ligula eget dolor. Aenean massa. \
                    Cum sociis natoque penatibus et magnis dis parturient \
                    montes, nascetur ridiculus mus. Donec quam felis, \
                    ultricies nec, pellentesque eu, pretium quis, sem. ",
            category=self.first_category,
            image="http://testimage.com"
        )
        self.first_article.save()

    def test_create_category_using_models(self):
        """
        Test that a new category can be created
        using the Category model
        """

        category_count = Category.objects.count()
        self.assertEqual(category_count, 1)

        category = Category(
            name="Lifestyle"
        )
        category.save()

        new_category_count = category_count = Category.objects.count()
        self.assertEqual(new_category_count, 2)

    def test_create_article_using_models(self):
        """
        Test that a new article can be created
        using the Article model
        """

        article_count = Article.objects.count()
        self.assertEqual(article_count, 1)

        article = Article(
            writer=self.admin,
            title="Test Article 2",
            content="Lorem ipsum dolor sit amet, consectetuer adipiscing \
                    elit. Aenean commodo ligula eget dolor. Aenean massa. \
                    Cum sociis natoque penatibus et magnis dis parturient \
                    montes, nascetur ridiculus mus. Donec quam felis, \
                    ultricies nec, pellentesque eu, pretium quis, sem. ",
            category=self.first_category,
            image="http://testimage.com"
        )
        article.save()

        new_article_count = article_count = Article.objects.count()
        self.assertEqual(new_article_count, 2)
