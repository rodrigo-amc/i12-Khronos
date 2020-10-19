from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# En Django (MTV) las vistas son los controladores de MVC
# Cada función dentro de este módulo, representa un controlador


# El framework reconoce automaticamente la carpeta "templates".
# Solo indico la subcarpeta/archivo.html

@login_required
def menuPrincipal(request):
    return render(request, 'Pedidos/menu.html')

@login_required
def proveedores(request):
    return render(request, 'Pedidos/proveedores.html')

@login_required
def pedidos(request):
    return render(request, 'Pedidos/pedidos.html')

@login_required
def ingresos(request):
    return render(request, 'Pedidos/ingresos.html')


def cerrarSesion(request):
    return HttpResponse('cerrarSesión')






