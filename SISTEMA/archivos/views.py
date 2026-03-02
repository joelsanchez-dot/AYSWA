from django.shortcuts import render, redirect, get_object_or_404
from .models import Archivo
from .forms import ArchivoForm

def lista_archivos(request):
    archivos = Archivo.objects.all()
    return render(request, 'archivos/lista.html', {'archivos': archivos})

def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ArchivoForm()
    return render(request, 'archivos/subir.html', {'form': form})

def editar_archivo(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES, instance=archivo)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ArchivoForm(instance=archivo)
    return render(request, 'archivos/editar.html', {'form': form})

def eliminar_archivo(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    archivo.delete()
    return redirect('lista')