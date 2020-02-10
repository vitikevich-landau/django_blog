from django.shortcuts import render

from blog.models import Post


def lists(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/details.html', {'post': post})
