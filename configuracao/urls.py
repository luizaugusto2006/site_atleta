from django.contrib import admin
from django.urls import path
from core.views import home
from django.conf import settings # Adicione esta linha
from django.conf.urls.static import static # Adicione esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # ISSO É O QUE FALTA PARA A RENDER ACHAR AS FOTOS NO DEPLOY
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)