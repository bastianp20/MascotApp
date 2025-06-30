from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registrar_veterinario  
from .models import registrar_veterinario as VetModel, MiembroEquipo  # Importamos el modelo real de la base de datos y se le cambia el nombre para evitar la colision de datos 

# Vista principal del sitio
def index(request):
    return render(request, 'index.html')

# Vista del perfil del veterinario
def perfil_veterinario(request):
    # simulacion de obtencion del usuario 
    veterinario = VetModel.objects.first()  # se está tomando el primer usuario que está en la base de datos. 

    # Si el veterinario pertenece a un centro veterinario, mostramos los miembros del equipo.
    if veterinario.veterinario_tipo == "CLIN":
        miembros = MiembroEquipo.objects.all()  # Luego puedes filtrar por centro si asocias miembros a un veterinario específico
    else:
        miembros = []  # No se muestran miembros para veterinarios independientes

    # 🔽 Enviamos tanto al veterinario como a sus miembros al HTML para mostrar su información.
    return render(request, 'veterinario.html', {
        'veterinario': veterinario,
        'miembros': miembros
    })

# Vista para el registro de veterinarios
def registro_veterinarios(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        email = request.POST['email']
        institucion = request.POST['institucion']
        certificado = request.FILES['certificado']
        tipo = request.POST.get('tipo_veterinario', 'IND')  # Por defecto 'IND' si no viene nada
        centro = request.POST.get('nombre_centro', '')

        # 🔽 Creamos el objeto veterinario en la base de datos
        VetModel.objects.create(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            email=email,
            institucion=institucion,
            certificado=certificado,
            veterinario_tipo=tipo,
            nombre_centro=centro if tipo == "CLIN" else '',
            verificado=True,  # Por ahora todos son verificados automáticamente (modo prueba)
            contraseña='1234'  # Contraseña temporal
        )
        return redirect('inicio_vet')  # Redirigimos al inicio (o login) del veterinario

    return render(request, 'registro_veterinarios.html')

# Vista del inicio de sesión del veterinario
def inicio_vet(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')

        try:
            vet = registrar_veterinario.objects.get(email=email, contraseña=contraseña)
            # Si llega aquí, el veterinario existe y es válido
            return render(request, 'veterinario.html', {'veterinario': vet})
        except registrar_veterinario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'inicio_vet.html')
