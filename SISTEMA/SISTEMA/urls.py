from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscripciones/', include('inscripciones.urls')),
    path('', include('alumnos.urls')),
    path('becas/', include('becas.urls')),
    path('cupones/', include('SISTEMA.cupones.urls')),
   path('', include('SISTEMA.foro_alumnos.urls')), # <--- También aquí agrega "SISTEMA."
]


