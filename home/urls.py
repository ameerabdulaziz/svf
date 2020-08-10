from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('contact-us', TemplateView.as_view(template_name='contact.html'), name='contact-us'),
]
