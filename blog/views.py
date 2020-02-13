from django.shortcuts import render, redirect
from django.views.generic import View

from blog.forms import TagForm, PostForm
from blog.mixins import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from blog.models import Post, Tag


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


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
