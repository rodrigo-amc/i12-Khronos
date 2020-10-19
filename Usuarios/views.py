from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def logIn(request):
    if request.user.is_authenticated:
        return redirect('/menu')
    else:
        #redirigir = redirect('accounts/login')
        return redirect('accounts/login')

@login_required
def usuarios(request):
    if request.user.is_superuser:
        #is_superuser es un campo en la tabla de usuarios con valores 0 y 1. 1=verdadero 0=falso
        return render(request, 'Usuarios/usuarios.html')
    else:
        return HttpResponse('Solo Disponible Para Usuario Administrador')