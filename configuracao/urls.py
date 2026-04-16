from django.contrib import admin
from django.urls import path, re_path # Adicionamos re_path aqui
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve # Importação essencial para produção

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Esta configuração abaixo substitui o seu IF/ELSE anterior
# Ela funciona tanto no seu PC quanto na Render
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]