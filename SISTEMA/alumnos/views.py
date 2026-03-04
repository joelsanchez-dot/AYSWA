from django.shortcuts import render
from .models import Cita

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'alumnos/lista.html', {'citas': citas})

def agregar_cita(request):
    return render(request, 'alumnos/agregar.html')