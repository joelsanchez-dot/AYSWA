from django.urls import path
from . import views

urlpatterns = [
    path('', views.CitaListView.as_view(), name='lista_citas'),
    path('nueva/', views.CitaCreateView.as_view(), name='crear_cita'),
    path('editar/<int:pk>/', views.CitaUpdateView.as_view(), name='editar_cita'),
    path('eliminar/<int:pk>/', views.CitaDeleteView.as_view(), name='eliminar_cita'),
]