from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('agregar/', views.agregar_cita, name='agregar_cita'),
]