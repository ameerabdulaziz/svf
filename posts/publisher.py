from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView


class PublisherCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.publisher = self.request.user
        instance.save()
        return super().form_valid(form)


class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.publisher = self.request.user
        instance.save()
        return super().form_valid(form)
