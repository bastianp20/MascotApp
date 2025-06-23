from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Veterinario
# Create your views here.
def index(request):
    return render(request, 'index.html')

def perfil_veterinario(request):
    return render(request, 'veterinario.html',{
        'form': UserCreationForm
    }) 

def registro_veterinarios(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        email = request.POST['email']
        institucion = request.POST['institucion']
        certificado = request.FILES['certificado']

        Veterinario.objects.create(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            email=email,
            institucion=institucion,
            certificado=certificado,
            verificado=True,  # a este campo le colocamos True por mientras ya que estamos en epocas de prueba
            contraseña='1234'  # Contraseña temporal
        )
        return redirect('inicio_vet') # esto nos retorna al login de los vet 

    return render(request, 'registro_veterinarios.html')

def inicio_vet(request):
    return render(request, 'inicio_vet.html')