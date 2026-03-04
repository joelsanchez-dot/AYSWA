from django.db import models

class Archivo(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='archivos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre