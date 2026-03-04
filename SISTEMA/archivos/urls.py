from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_archivos, name='lista_archivos'),
    path('crear/', views.crear_archivo, name='crear_archivo'),
    path('editar/<int:id>/', views.editar_archivo, name='editar_archivo'),
    path('eliminar/<int:id>/', views.eliminar_archivo, name='eliminar_archivo'),
    path('descargar/<int:id>/', views.descargar_archivo, name='descargar_archivo'),
]