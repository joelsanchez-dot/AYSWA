from django.shortcuts import render
from .models import Paciente, Cita

def lista_citas(request):
    citas = Cita.objects.all()
    # Asegúrate de que el HTML esté en alumnos/templates/alumnos/lista.html
    return render(request, 'alumnos/lista.html', {'citas': citas})