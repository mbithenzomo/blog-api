# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='Technology'),
            preserve_default=False,
        ),
    ]