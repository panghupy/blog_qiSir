from django.contrib import admin
from .models import BlogArticles,Category,Comment
# Register your models here.









admin.site.register(BlogArticles)
admin.site.register(Category)
admin.site.register(Comment)