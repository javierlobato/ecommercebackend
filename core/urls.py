from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Redirige a las rutas de la app `api`
    path('api-auth/', include('rest_framework.urls')),  # Para autenticación de DRF
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

