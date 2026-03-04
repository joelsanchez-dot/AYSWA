from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnos.urls')),
    path('becas/', include('becas.urls')),
    path('cupones/', include('cupones.urls')),
    # Esta línea redirige la raíz a cupones si así lo deseas
    # path('', RedirectView.as_view(url='cupones/', permanent=True)), 
]