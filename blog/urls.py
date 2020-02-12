from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_lists, name='lists_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_details_url'),
    path('tags/', tags_list, name='tags_url'),
    path('tags/<str:slug>', TagDetail.as_view(), name='tag_details_url'),
]