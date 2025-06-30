# MascotApp/forms.py
from django import forms
from .models import registrar_veterinario

class RegistroVeterinarioForm(forms.ModelForm):
    class Meta:
        model = registrar_veterinario
        fields = ['nombre', 'apellido', 'rut', 'email', 'certificado', 'institucion', 'verificado']
