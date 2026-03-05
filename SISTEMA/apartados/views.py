from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Producto

def home(request):
    return render(request, 'apartados/home.html')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'activo']

def producto_list(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'apartados/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'apartados/producto_form.html', {'form': form, 'titulo': 'Nuevo producto'})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'apartados/producto_form.html', {'form': form, 'titulo': 'Editar producto'})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'apartados/producto_delete.html', {'producto': producto})