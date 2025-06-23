# MascotApp/forms.py
from django import forms
from .models import Veterinario

class RegistroVeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'apellido', 'rut', 'email', 'certificado', 'institucion', 'verificado']
