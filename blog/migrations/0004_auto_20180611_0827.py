# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-11 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=None, null=True),
        ),
    ]
