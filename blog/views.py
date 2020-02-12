from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from blog.forms import TagForm
from blog.models import Post, Tag


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/details.html'


def posts_lists(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            return redirect(bound_form.save())

        return render(request, 'blog/tag_create.html', {'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})
