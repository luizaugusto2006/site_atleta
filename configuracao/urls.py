from django.contrib import admin
from django.urls import path, re_path
from core.views import home, media_serve, pagina_404

handler404 = 'core.views.pagina_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^media/(?P<path>.*)$', media_serve, name='media_serve'),
]
