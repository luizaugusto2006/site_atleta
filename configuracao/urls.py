from django.contrib import admin
from django.urls import path
from core.views import home
from django.conf import settings # Adicione esta linha
from django.conf.urls.static import static # Adicione esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Este bloco abaixo é o que faz a mágica das fotos aparecerem
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)