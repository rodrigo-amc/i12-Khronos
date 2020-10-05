from django.shortcuts import render, HttpResponse

# Create your views here.
# En Django (MTV) las vistas son los controladores de MVC
# Cada función dentro de este módulo, representa un controlador

def logIn(request):
    return render(request, 'Pedidos/login.html')
    # El framework reconoce automaticamente la carpeta "templates". Solo indico la subcarpeta.
    #

def menuPrincipal(request):
    return render(request, 'Pedidos/menu.html')

def usuarios(request):
    return render(request, 'Pedidos/usuarios.html')

def proveedores(request):
    return render(request, 'Pedidos/proveedores.html')

def pedidos(request):
    return HttpResponse('pedidos')

def ingresos(request):
    return HttpResponse('ingresos')

def cerrarSesion(request):
    return HttpResponse('cerrarSesión')






