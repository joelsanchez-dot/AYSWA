from django.db import models

class Materia(models.Model):
    ESTATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Cursando', 'Cursando'),
        ('Aprobada', 'Aprobada'),
    ]
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    horario = models.CharField(max_length=50)
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='Pendiente')
    calificacion = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre