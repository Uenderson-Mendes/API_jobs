from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import api_root  # Importa a view

urlpatterns = [
    path('', api_root, name='api-root'),  # Página inicial HTML da API
    path('admin/', admin.site.urls),

    # Rotas de API dos apps
    path('api/users/', include('users.urls')),
    path('api/companies/', include('companies.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/applications/', include('applications.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api-auth/', include('rest_framework.urls')),  # login/logout DRF
]

# Adicionar suporte a arquivos de mídia no ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
