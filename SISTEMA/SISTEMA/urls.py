from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnosJavier.urls')),   # Tu app alumnosJavier
    path('alumnos/', include('alumnos.urls')), # App alumnos del profe
    path('becas/', include('becas.urls')),     # App becas del profe
]
