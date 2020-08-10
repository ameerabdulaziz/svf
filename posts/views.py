from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView

from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment
from posts.publisher import PublisherCreateView, PublisherUpdateView, PublisherDeleteView


class PostListView(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        try:
            q = self.request.GET.get('q')
            object_list = self.model.objects.filter(title__icontains=q)
        except:
            object_list = self.model.objects.all()
        return object_list


class PostCreateView(PublisherCreateView):
    model = Post
    form_class = PostForm


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context
    
    def post(self, *args, **kwargs):
        form = CommentForm()
        if form.is_valid(self):
            print('valid')
        return redirect('posts:post-list')


class PostUpdateView(PublisherUpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(PublisherDeleteView):
    model = Post


class CommentCreateView(CreateView):
    model = Comment
    http_method_names = ['post']
    form_class = PostForm
    # template_name = 'posts/post_detail.html'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.post = Post.objects.get(id=self.kwargs['pk'])
        instance.save()
        return super(CommentCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('accounts:profile_detail', {'pk': self.kwargs['pk']})
