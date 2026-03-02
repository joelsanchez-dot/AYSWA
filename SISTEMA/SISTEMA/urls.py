from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cupones/', include('cupones.urls')),
    # Esta línea soluciona tu primer error de la imagen
    path('', RedirectView.as_view(url='cupones/', permanent=True)), 
]