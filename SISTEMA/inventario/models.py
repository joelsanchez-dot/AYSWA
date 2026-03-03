from django.db import models

class Computadora(models.Model):
    numero_serie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} - {self.numero_serie}"


class Mobiliario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo