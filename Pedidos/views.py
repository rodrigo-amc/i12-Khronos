from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Importo formularios
from .forms import frProveedor

# Create your views here.
# En Django (MTV) las vistas son los controladores de MVC
# Cada función dentro de este módulo, representa un controlador


# El framework reconoce automaticamente la carpeta "templates".
# Solo indico la subcarpeta/archivo.html

@login_required
def menuPrincipal(request):
    return render(request, 'Pedidos/menu.html')

#region Controladores Proveedores 
@login_required
def proveedores(request):
    return render(request, 'Pedidos/proveedores.html')

@login_required
def provNuevo(request):

    formulario = frProveedor()

    if request.method == 'POST':
        frpost = frProveedor(request.POST)
        if frpost.is_valid():
            frpost.save()
            return redirect('/proveedores')
        else:
            for mensaje in frpost.errors:
                messages.error(request, frpost.errors[mensaje])
                return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor': frpost})
    else:
        return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor': formulario})
        
#endregion

@login_required
def pedidos(request):
    return render(request, 'Pedidos/pedidos.html')

@login_required
def ingresos(request):
    return render(request, 'Pedidos/ingresos.html')


def cerrarSesion(request):
    return HttpResponse('cerrarSesión')






