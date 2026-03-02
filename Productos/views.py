from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductoApartado

def listar_productos(request):
    productos = ProductoApartado.objects.all()
    if request.method == 'POST':
        ProductoApartado.objects.create(
            nombre_cliente=request.POST['cliente'],
            producto=request.POST['producto'],
            precio_total=request.POST['precio'],
            monto_apartado=request.POST['apartado']
        )
        return redirect('listar_productos')
    return render(request, 'Productos/index.html', {'productos': productos})

def editar_producto(request, pk):
    producto = get_object_or_404(ProductoApartado, pk=pk)
    if request.method == 'POST':
        producto.nombre_cliente = request.POST['cliente']
        producto.producto = request.POST['producto']
        producto.precio_total = request.POST['precio']
        producto.monto_apartado = request.POST['apartado']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'Productos/editar.html', {'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(ProductoApartado, pk=pk)
    producto.delete()
    return redirect('listar_productos')