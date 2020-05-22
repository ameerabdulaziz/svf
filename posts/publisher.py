from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView


class PublisherCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.publisher = self.request.user
        instance.save()
        return super().form_valid(form)


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(publisher=self.request.user)


class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(publisher=self.request.user)
