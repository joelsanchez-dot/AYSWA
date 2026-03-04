from django import forms
from .models import Alumno, Materia, Inscripcion


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = "__all__"


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ["alumno", "materia", "calificacion"]