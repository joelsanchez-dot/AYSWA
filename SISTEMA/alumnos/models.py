from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Alumno(models.Model):
    nombre = models.CharField(max_length=150)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

    # ===== LÓGICA DE NEGOCIO =====

    def creditos_aprobados(self):
        return sum(
            ins.materia.creditos
            for ins in self.inscripciones.filter(
                estado=Inscripcion.Estado.APROBADA
            )
        )

    def total_creditos(self):
        return Materia.objects.aggregate(
            total=models.Sum("creditos")
        )["total"] or 0

    def porcentaje_avance(self):
        total = self.total_creditos()
        if total == 0:
            return 0
        return round((self.creditos_aprobados() / total) * 100, 2)


class Materia(models.Model):
    nombre = models.CharField(max_length=150)
    clave = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.nombre} ({self.creditos} créditos)"


class Inscripcion(models.Model):

    class Estado(models.TextChoices):
        EN_CURSO = "EN_CURSO", "En curso"
        APROBADA = "APROBADA", "Aprobada"
        REPROBADA = "REPROBADA", "Reprobada"

    alumno = models.ForeignKey(
        Alumno,
        related_name="inscripciones",
        on_delete=models.CASCADE
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE
    )
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.EN_CURSO
    )
    calificacion = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        unique_together = ("alumno", "materia")

    def save(self, *args, **kwargs):
        if self.calificacion is not None:
            if self.calificacion >= 6:
                self.estado = self.Estado.APROBADA
            else:
                self.estado = self.Estado.REPROBADA
        super().save(*args, **kwargs)