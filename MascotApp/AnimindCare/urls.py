from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('veterinario/', views.perfil_veterinario, name='veterinario'),
    path('registro_veterinarios/', views.registro_veterinarios, name='registro_veterinarios'),
    path('inicio_vet/', views.inicio_vet, name='inicio_vet')
]
