from django.shortcuts import render, redirect, get_object_or_404
from .models import Archivo
from django import forms
from django.http import FileResponse
import os


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'archivo']


def lista_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, 'archivos/lista.html', {'archivos': archivos})


def crear_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_archivos')
    else:
        form = ArchivoForm()

    return render(request, 'archivos/form.html', {'form': form})


def editar_archivo(request, id):
    archivo = get_object_or_404(Archivo, id=id)

    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES, instance=archivo)
        if form.is_valid():
            form.save()
            return redirect('lista_archivos')
    else:
        form = ArchivoForm(instance=archivo)

    return render(request, 'archivos/form.html', {'form': form})


def eliminar_archivo(request, id):
    archivo = get_object_or_404(Archivo, id=id)
    archivo.delete()
    return redirect('lista_archivos')
def descargar_archivo(request, id):
    archivo = get_object_or_404(Archivo, id=id)
    ruta = archivo.archivo.path
    return FileResponse(open(ruta, 'rb'), as_attachment=True)