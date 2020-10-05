from django.shortcuts import render, HttpResponse

# Create your views here.
# En Django (MTV) las vistas son los controladores de MVC
# Cada función dentro de este módulo, representa un controlador

def logIn(request):
    return HttpResponse('Página Para Login')

def menuPrincipal(request):
    return HttpResponse('menuPrincipal')

def usuarios(request):
    return HttpResponse('usuarios')

def proveedores(request):
    return HttpResponse('proveedores')

def pedidos(request):
    return HttpResponse('pedidos')

def ingresos(request):
    return HttpResponse('ingresos')

def cerrarSesion(request):
    return HttpResponse('cerrarSesión')






