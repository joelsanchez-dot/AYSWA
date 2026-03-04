from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, Materia
from .forms import AlumnoForm, MateriaForm, InscripcionForm


# ===============================
# HOME
# ===============================

def home(request):
    return render(request, "alumnos/home.html")


# ===============================
# ALUMNOS
# ===============================

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, "alumnos/lista-alumno.html", {"alumnos": alumnos})


def alumno_detail(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, "alumnos/detalle-alumno.html", {"alumno": alumno})


def alumno_create(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("alumno_list")
    return render(request, "alumnos/formulario-alumno.html", {"form": form})


# ===============================
# MATERIAS
# ===============================

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, "alumnos/lista-materia.html", {"materias": materias})


def materia_create(request):
    form = MateriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("materia_list")
    return render(request, "alumnos/formulario-materia.html", {"form": form})


# ===============================
# INSCRIPCIÓN
# ===============================

def inscripcion_create(request):
    form = InscripcionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("alumno_list")
    return render(request, "alumnos/formulario-inscripcion.html", {"form": form})