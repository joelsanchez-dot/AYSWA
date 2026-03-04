from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    ESTADOS = [('P', 'Pendiente'), ('C', 'Completada'), ('X', 'Cancelada')]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(max_length=300)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"