from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Importo el formulario de forms.py
from .forms import fr_CrearUsuario

# lo uso para los mensajes de validaciones en formularios
from django.contrib import messages

# Lo uso para listar los usuarios en la vista "usuarios"
from django.contrib.auth.models import User



# Create your views here.

# Controlador para login
def logIn(request):
    if request.user.is_authenticated:
        return redirect('/menu')
    else:
        #redirigir = redirect('accounts/login')
        return redirect('accounts/login')

#Controlador para acceder al menu de usuarios
@login_required
def usuarios(request):

    

    if request.user.is_superuser:
        #is_superuser es un campo en la tabla de usuarios con valores 0 y 1. 1=verdadero 0=falso

        # en listUsuarios almaceno todos los usuarios y se los paso al template para listarlos
        contexto = {
            'listUsuarios': User.objects.all()
        }

        return render(request, 'Usuarios/usuarios.html', contexto)

    # Si el usuario no es administrador
    else:
        return HttpResponse('Solo Disponible Para Usuario Administrador')


#Controlador para Crear Nuevo Usuario
@login_required
def usuarioNuevo(request):
    if request.user.is_superuser:
        contexto = {
            #Instancio un formulario vacío que se muestra
            #cuando se carga la página por GET
            'formulario': fr_CrearUsuario(),
        }

        #Si el request es por POST, significa que se usó el botón para enviar el formulario
        #Entonces se procesa el contenido del formulario.
        if request.method == 'POST':
            #Instancio un formulario y le paso por parámetro el contenido del formulario
            formulario = fr_CrearUsuario(request.POST)

            #Si los valores del formulario son válidos se guarda en bd
            if formulario.is_valid():
                formulario.save()
                return redirect('/usuarios')
                
            else:
                for mensaje in formulario.error_messages:
                    messages.error(request, formulario.error_messages[mensaje])
                    return render(request, 'Usuarios/usuarioNuevo.html', {'formulario': formulario})

        # Si el request es por GET devuelve el formulario vacío
        return render(request, 'Usuarios/usuarioNuevo.html', contexto)

    # Si el usuario no es administrador
    else:
        return HttpResponse('Solo Disponible Para Usuario Administrador')