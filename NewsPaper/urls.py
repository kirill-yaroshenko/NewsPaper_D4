from django.contrib import admin
from django.urls import path, include
from .view import multiply


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('multiply/', multiply),
]
