from django.views.generic import ListView, DetailView, DeleteView

from posts.forms import PostForm
from posts.models import Post
from posts.publisher import PublisherCreateView, PublisherUpdateView, PublisherDeleteView


class PostListView(ListView):
    model = Post


class PostCreateView(PublisherCreateView):
    model = Post
    form_class = PostForm


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(PublisherUpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(PublisherDeleteView):
    model = Post
