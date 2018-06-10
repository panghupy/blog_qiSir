from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import BlogArticles

# Create your views here.
def index(request):
    return render(request,'index.html')


def post_list(request):
    post_list = BlogArticles.objects.all()
    return render(request,'list.html',{'post_list':post_list})


def detail(request,pid):
    post = get_object_or_404(BlogArticles,id=pid)
    return render(request,'show.html',{'post':post})
