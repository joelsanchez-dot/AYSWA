from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_dudas, name='lista_dudas'),
    path('nueva/', views.crear_duda, name='crear_duda'),
]