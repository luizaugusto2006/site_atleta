import os
from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from .models import Atleta

def home(request):
    atleta = Atleta.objects.first()
    estatistica = atleta.estatisticas.first() if atleta else None
    estatisticas = atleta.estatisticas.all() if atleta else []
    return render(request, 'index.html', {
        'atleta': atleta,
        'estatistica': estatistica,
        'estatisticas': estatisticas,
    })

def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404("Arquivo não encontrado")
    return FileResponse(open(file_path, 'rb'))

def pagina_404(request, exception):
    return render(request, '404.html', status=404)
