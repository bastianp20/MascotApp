# MascotApp/forms.py
from django import forms
from .models import veterinario

class RegistroVeterinarioForm(forms.ModelForm):
    class Meta:
        model = veterinario
        fields = ['nombre', 'apellido', 'rut', 'email', 'certificado', 'institucion', 'verificado']
