# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Main blog page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Individual post page
    path('create/', views.create_post, name='create_post'),
]