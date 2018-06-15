from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    nikename = models.CharField(verbose_name='昵称', max_length=30)
    phone = models.CharField(verbose_name='手机号', max_length=11)

    class Meta:
        verbose_name = '博客用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
