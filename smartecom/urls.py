from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('perfil', include('apps.perfil.urls')),
    path('admin/', admin.site.urls),
]
