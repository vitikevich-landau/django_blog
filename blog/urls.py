from django.urls import path

from . import views

urlpatterns = [
    path('', views.lists, name='lists_url'),
    path('post/<str:slug>/', views.details, name='details_url'),
]