from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_lists, name='lists_url'),
    path('post/<str:slug>/', views.post_details, name='post_details_url'),
    path('tags/', views.tags_list, name='tags_url'),
    path('tags/<str:slug>', views.tag_detail, name='tag_details_url'),
]