from django.contrib import admin
from .models import Paciente, Cita

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')
    search_fields = ('nombre',)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha')