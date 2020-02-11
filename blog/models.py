from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    #   Many to many
    #   tags
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def get_absolute_url(self):
        return reverse('post_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title or "None"}'


class Tag(models.Model):
    #   posts
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title or "None"}'
