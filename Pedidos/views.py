from django.shortcuts import render, HttpResponse

# Create your views here.
# En Django (MTV) las vistas son los controladores de MVC
# Cada función dentro de este módulo, representa un controlador


# El framework reconoce automaticamente la carpeta "templates".
# Solo indico la subcarpeta/archivo.html


def menuPrincipal(request):
    return render(request, 'Pedidos/menu.html')


def proveedores(request):
    return render(request, 'Pedidos/proveedores.html')


def pedidos(request):
    return render(request, 'Pedidos/pedidos.html')


def ingresos(request):
    return render(request, 'Pedidos/ingresos.html')


def cerrarSesion(request):
    return HttpResponse('cerrarSesión')






