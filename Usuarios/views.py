from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def logIn(request):
    redirigir = redirect('accounts/login')
    return redirigir

@login_required
def usuarios(request):
    if reques.user.is_superuser:
        #is_superuser es un campo en la tabla de usuarios con valores 0 y 1. 1=verdadero 0=falso
        return render(request, 'usuarios.html')
    else:
        return HttpResponse('Solo Disponible Para Usuario Administrador')