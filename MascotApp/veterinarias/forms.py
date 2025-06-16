# MascotApp/forms.py
from django import forms
from .models import veterinarios

class RegistroVeterinarioForm(forms.ModelForm):
    class Meta:
        model = veterinarios
        fields = ['Nombre', 'Apellido', 'Email', 'Certificado']
