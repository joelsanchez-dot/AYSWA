from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnos/', views.alumno_list, name='alumno_list'),
    path('alumnos/<int:pk>/', views.alumno_detail, name='alumno_detail'),
    path('alumnos/nuevo/', views.alumno_create, name='alumno_create'),

    path('materias/', views.materia_list, name='materia_list'),
    path('materias/nuevo/', views.materia_create, name='materia_create'),

    path('inscripcion/nueva/', views.inscripcion_create, name='inscripcion_create'),
]