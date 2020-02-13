from django import forms
from blog.models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'some-class'})
    # slug.widget.attrs.update({'class': 'some-class'})

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
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Такой slug "{new_slug}" уже есть')

        return new_slug
