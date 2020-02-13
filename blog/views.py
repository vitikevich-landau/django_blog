from django.shortcuts import render, redirect
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.mixins import ObjectDetailMixin, ObjectCreateMixin
from blog.models import Post, Tag


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/details.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create_form.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


def posts_lists(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})
