import os
from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from .models import Atleta

def home(request):
    atleta = Atleta.objects.first()
    return render(request, 'index.html', {'atleta': atleta})

def media_serve(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404("Arquivo não encontrado")
    return FileResponse(open(file_path, 'rb'))