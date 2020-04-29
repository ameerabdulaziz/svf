from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
