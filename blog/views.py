from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import BlogArticles, Comment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def post_list(request):
    post_list = BlogArticles.objects.all()
    return render(request, 'list.html', {'post_list': post_list})


def detail(request, pid):
    post = get_object_or_404(BlogArticles, id=pid)
    comment_list = Comment.objects.filter(post=pid)
    context = {
        'post': post,
        'comment_list': comment_list,
    }
    return render(request, 'show.html', context)


def comment(request, pid):
    post = get_object_or_404(BlogArticles, id=pid)
    comment_list = Comment.objects.filter(post=pid)
    comment = Comment()
    comment.post = post
    comment.content = request.POST.get('content', '')
    comment.user = request.user
    comment.save()
    context = {
        'post': post,
        'comment_list': comment_list,
    }
    return render(request, 'show.html', context)
