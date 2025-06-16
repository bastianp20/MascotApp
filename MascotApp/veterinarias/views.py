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
            return render(request, 'registro_exitoso.html')
    else:
        form = RegistroVeterinarioForm()
    return render(request, 'registro_veterinarios.html', {'form': form})