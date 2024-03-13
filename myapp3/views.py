from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from myapp3.models import Post, Author


# Create your views here.

def index(request):
    return HttpResponse("MAin")


def about(request):
    return HttpResponse("About us")


def user_posts(request, user_id):
    user = get_object_or_404(Author, pk=user_id)
    posts =Post.objects.filter(author=user_id)
    context = {'title': 'Посты', 'posts': posts, 'author': user}
    return render(request, 'myapp3/posts.html', context=context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'title': 'Пост', 'post': post}
    return render(request, 'myapp3/post.html', context=context)