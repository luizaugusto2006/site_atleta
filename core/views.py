from django.shortcuts import render
from .models import Atleta

def home(request):
    # Buscamos o primeiro atleta cadastrado no banco
    atleta = Atleta.objects.first() 
    return render(request, 'index.html', {'atleta': atleta})