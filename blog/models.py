from time import time

from django.db import models
from django.urls import reverse

from django.utils.text import slugify


def generate_slug(s):
    return slugify(s, allow_unicode=True) + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    #   Many to many
    #   tags
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)

    def get_absolute_url(self):
        return reverse('post_details_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'None'

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    #   posts
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_details_url', kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = generate_slug(self.title)
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'None'
