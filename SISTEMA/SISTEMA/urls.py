from django.contrib import admin # Importa el panel de admin
from django.urls import path # Importa la herramienta para crear rutas
from alumnos.views import reporte_escolar # Importa la lógica que acabas de escribir

urlpatterns = [
    # Dirección para gestionar los datos (ej: 127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),
    
    # Dirección para ver el reporte (ej: 127.0.0.1:8000/reporte/)
    path('reporte/', reporte_escolar),
]