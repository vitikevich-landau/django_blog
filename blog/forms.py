from django import forms
from blog.models import Tag, Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'some-class'}),
            'slug': forms.TextInput(attrs={'class': 'some-class'}),
            'body': forms.Textarea(attrs={'class': 'some-class'}),
            'tags': forms.SelectMultiple(attrs={'class': 'some-class'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Поле slug не может быть "create"')

        return new_slug


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'some-class'}),
            'slug': forms.TextInput(attrs={'class': 'some-class'})
        }

    def clean_slug(self):
        #   use self.cleaned_data.get('slug')
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Поле slug не может быть "create"')
        #   Проверка есть ли такой slug
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Такой slug "{new_slug}" уже есть')

        return new_slug
