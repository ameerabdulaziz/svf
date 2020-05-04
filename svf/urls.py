from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from svf import settings

urlpatterns = [
    path('', include('home.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
