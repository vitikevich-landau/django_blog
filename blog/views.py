from django.shortcuts import render

from blog.models import Post, Tag


def posts_lists(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/details.html', {'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', {'tag': tag})
