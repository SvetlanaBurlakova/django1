from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from myapp3.forms import PostForm, AuthorForm
from myapp3.models import Post, Author


# Create your views here.

def index(request):
    return HttpResponse("MAin")


def about(request):
    return HttpResponse("About us")


def user_posts(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = Author.objects.get(pk=user_id)
            Post(**form.cleaned_data, author=author).save()
    else:
        form = PostForm()
    user = get_object_or_404(Author, pk=user_id)
    posts =Post.objects.filter(author=user_id)

    context = {'title': 'Посты', 'posts': posts, 'author': user}
    return render(request, 'myapp3/posts.html', context=context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'title': 'Пост', 'post': post}
    return render(request, 'myapp3/post.html', context=context)


def authors(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
           Author(**form.cleaned_data).save()
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {
        'title': 'Авторы',
        'authors': authors,
        'form': form,
    }
    return render(request, 'myapp3/author.html', context=context)