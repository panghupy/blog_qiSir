from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='博客分类')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogArticles(models.Model):
    title = models.CharField(max_length=50, verbose_name='博客标题')
    author = models.ForeignKey(User, verbose_name='博客作者')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, verbose_name='博客分类')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
