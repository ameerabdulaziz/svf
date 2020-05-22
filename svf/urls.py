from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from svf import settings

project_urls = [
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
]

third_party_urls = [

]

admin_urls = [
    path('admin/', admin.site.urls),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]

urlpatterns = project_urls + third_party_urls + admin_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
