from django.urls import path

from posts.api import viewsets

# app_name = 'posts'

urlpatterns = [
    path('posts/', viewsets.PostListCreateAPIView.as_view(), name='post-list-api'),
]
