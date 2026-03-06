from django.shortcuts import render, redirect
from .models import Duda

def lista_dudas(request):
    # Trae todas las dudas de la más reciente a la más antigua
    dudas = Duda.objects.all().order_by('-fecha_publicacion')
    return render(request, 'foro_alumnos/lista_dudas.html', {'dudas': dudas})

def crear_duda(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        Duda.objects.create(titulo=titulo, contenido=contenido)
        return redirect('lista_dudas')
    return render(request, 'foro_alumnos/crear_duda.html')