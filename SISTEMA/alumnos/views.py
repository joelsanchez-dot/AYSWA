from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cita

# LISTAR CITAS (Lectura)
class CitaListView(ListView):
    model = Cita
    template_name = 'alumnos/lista_citas.html'
    context_object_name = 'citas'

# CREAR CITA (Alta)
class CitaCreateView(CreateView):
    model = Cita
    template_name = 'alumnos/form_cita.html'
    fields = ['paciente', 'fecha', 'hora', 'motivo', 'estado']
    success_url = reverse_lazy('lista_citas')

# EDITAR CITA (Modificar)
class CitaUpdateView(UpdateView):
    model = Cita
    template_name = 'alumnos/form_cita.html'
    fields = ['paciente', 'fecha', 'hora', 'motivo', 'estado']
    success_url = reverse_lazy('lista_citas')

# ELIMINAR CITA (Baja)
class CitaDeleteView(DeleteView):
    model = Cita
    template_name = 'alumnos/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_citas')