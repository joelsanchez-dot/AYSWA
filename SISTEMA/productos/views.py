from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# LISTAR PRODUCTOS
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

# CREAR PRODUCTO
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        fecha_apartado = request.POST['fecha_apartado']
        cliente = request.POST['cliente']

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            fecha_apartado=fecha_apartado,
            cliente=cliente
        )
        return redirect('lista_productos')

    return render(request, 'productos/crear.html')

# EDITAR PRODUCTO
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.fecha_apartado = request.POST['fecha_apartado']
        producto.cliente = request.POST['cliente']
        producto.save()
        return redirect('lista_productos')

    return render(request, 'productos/editar.html', {'producto': producto})

# ELIMINAR PRODUCTO
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')