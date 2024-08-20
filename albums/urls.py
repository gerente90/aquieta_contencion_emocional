# albums/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from albums import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("album_manager.urls")),
    path('accounts/', include('django.contrib.auth.urls')),  # Añadir las URLs de autenticación
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
