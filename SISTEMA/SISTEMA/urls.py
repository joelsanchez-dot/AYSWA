from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumnos/', include('alumna_jazmin.urls')),
]
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumnos.urls')),
]
>>>>>>> upstream/main
