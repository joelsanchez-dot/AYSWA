from django.shortcuts import render, redirect
from .models import Materia
from django.db.models import Sum

def lista_materias(request):
    materias = Materia.objects.all()
    
    # Cálculos de Avance y Gestión de Créditos
    total_creditos = materias.aggregate(Sum('creditos'))['creditos__sum'] or 0
    creditos_aprobados = materias.filter(estatus='Aprobada').aggregate(Sum('creditos'))['creditos__sum'] or 0
    
    # Porcentaje de avance
    avance = (creditos_aprobados / total_creditos * 100) if total_creditos > 0 else 0

    context = {
        'materias': materias,
        'total_creditos': total_creditos,
        'creditos_aprobados': creditos_aprobados,
        'avance': round(avance, 2)
    }
    return render(request, 'alumnos/lista.html', context)

def agregar_materia(request):
    if request.method == "POST":
        Materia.objects.create(
            nombre=request.POST['nombre'],
            creditos=request.POST['creditos'],
            horario=request.POST['horario'],
            estatus=request.POST['estatus'],
            calificacion=request.POST.get('calificacion', 0)
        )
        return redirect('lista_materias')
    return render(request, 'alumnos/agregar.html')

def editar_materia(request, id):
    materia = Materia.objects.get(id=id)
    if request.method == "POST":
        materia.nombre = request.POST['nombre']
        materia.creditos = request.POST['creditos']
        materia.horario = request.POST['horario']
        materia.estatus = request.POST['estatus']
        materia.calificacion = request.POST['calificacion']
        materia.save()
        return redirect('lista_materias')
    return render(request, 'alumnos/editar.html', {'materia': materia})

# eliminar_materia se queda igual
def eliminar_materia(request, id):
    materia = Materia.objects.get(id=id)
    materia.delete()
    return redirect('lista_materias')