from django.contrib import admin

# Register your models here.
from .models import registrar_veterinario, MiembroEquipo
admin.site.register(registrar_veterinario)
admin.site.register(MiembroEquipo)