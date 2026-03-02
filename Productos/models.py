from django.db import models

class ProductoApartado(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=200)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_apartado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apartado = models.DateField(auto_now_add=True)