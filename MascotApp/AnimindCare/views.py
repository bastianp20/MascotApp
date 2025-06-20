from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroVeterinarioForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def veterinario(request):
    return render(request, 'veterinario.html',{
        'form': UserCreationForm
    }) 

def registro_veterinarios(request):
    if request.method == 'POST':
        form = RegistroVeterinarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'registro_exitoso.html') # ésta por crearse esta página, que será para confirmar si el registro fue exitoso. 
    else:
        form = RegistroVeterinarioForm()
    return render(request, 'registro_veterinarios.html', {'form': form})

def inicio_vet(request):
    return render(request, 'inicio_vet.html')