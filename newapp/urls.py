from django.contrib import admin

from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path("admin/", admin.site.urls), 
  path("", include("posts.urls")),
  path('auth/', include('users.urls')),
  path('auth/', include('django.contrib.auth.urls')),
  path('pages/', include('pages.urls')),
  path('contact/', include('contacts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)