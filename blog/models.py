from django.db import models
from account.models import BlogUser


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='博客分类')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogArticles(models.Model):
    title = models.CharField(max_length=50, verbose_name='博客标题')
    author = models.ForeignKey(BlogUser, verbose_name='博客作者')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, verbose_name='博客分类')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(BlogArticles, verbose_name='评论的博客', )
    user = models.ForeignKey(BlogUser, verbose_name='评论作者')
    pub_date = models.DateTimeField(verbose_name='评论发布时间', auto_now=True)
    content = models.TextField(null=False, default='')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '评论'
        verbose_name_plural = verbose_name
