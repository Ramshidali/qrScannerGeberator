from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.views.static import serve
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(('scanner.urls'),namespace='scanner')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
