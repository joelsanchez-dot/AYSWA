from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_archivos, name='lista'),
    path('subir/', views.subir_archivo, name='subir'),
    path('editar/<int:pk>/', views.editar_archivo, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_archivo, name='eliminar'),
]