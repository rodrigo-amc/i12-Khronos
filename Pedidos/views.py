from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Importo formularios
from .forms import frProveedor, frCerveza
from .models import Proveedor, Cerveza

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
                 #No es un error, es problema del ide
    proveedores = Proveedor.objects.all()
    return render(request, 'Pedidos/proveedores.html', {'proveedores':proveedores})


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
                return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor': frpost, 'titulo':'Nuevo Proveedor'})
    else:
        return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor': formulario, 'titulo':'Nuevo Proveedor'})


@login_required
def provEditar(request, id):
    provID = Proveedor.objects.get(pk=id)
    frEditar = frProveedor()
    if request.method == 'GET':
        frEditar = frProveedor(instance=provID)
        return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor':frEditar, 'titulo':'Editar Proveedor'})
    else:
        frEditar = frProveedor(request.POST, instance=provID)

        if frEditar.is_valid():
            frEditar.save()
        else:
            for mensaje in frEditar.errors:
                messages.error(request, frEditar.errors[mensaje])
                return render(request, 'Pedidos/proveedoresForm.html', {'formProveedor': frEditar, 'titulo':'Editar Proveedor'})
        
        return redirect('/proveedores')


@login_required
def provBorrar(request, id):
    #return HttpResponse('ID Seleccionado: {}'.format(id))
    provID = Proveedor.objects.get(pk=id)
    provID.delete()
    return redirect('/proveedores')

#endregion Proveedores


#region Cervezas
@login_required
def cervezas(request):
    cs = Cerveza.objects.all()
    #region
    # cs es un "QuerySet", un iterable...
    # Cada elemento de "cs" representa un objeto de tipo Cerveza.
    # Cada Cerveza tiene el campo "proveedor", que es un querySet,
    # El campo proveedor es una colección ce objetos Proveedor.
    # Le paso al Template "cs" para listar las cervezas y sus
    # Proveedores.

    # Para entender el funcionamiento de QuerySet
    # https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/

    # Ojo, en el template no puedo usar paréntesis en los métodos
    # por ejemplo "all()"
    #endregion
    return render(request, 'Pedidos/cervezas.html', {'cervezas':cs})


@login_required
def cervNuevo(request):
    formulario = frCerveza()

    if request.method == 'POST':
        form = frCerveza(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cervezas')
        else:
            for mensaje in form.errors:
                messages.error(request, form.errors[mensaje])
                return render(request, 'Pedidos/cervezasForm.html', {'formCerveza': form, 'titulo':'Nueva Cerveza'})
    else:
        return render(request, 'Pedidos/cervezasForm.html', {'formCerveza':formulario, 'titulo':'Nueva Cerveza'})


@login_required
def cervEditar(request, id):
    cervEdit = Cerveza.objects.get(pk=id)
    frEditar = frCerveza()
    if request.method == 'GET':
        frEditar = frCerveza(instance=cervEdit)
        return render(request, 'Pedidos/cervezasForm.html', {'formCerveza':frEditar, 'titulo':'Editar Cerveza'})
    else:
        frEditar = frCerveza(request.POST, instance=cervEdit)

        if frEditar.is_valid():
            frEditar.save()
        else:
            for mensaje in frEditar.errors:
                messages.error(request, frEditar.errors[mensaje])
                return render(request, 'Pedidos/cervezasForm.html', {'formCerveza': frEditar, 'titulo':'Editar Cerveza'})
        
        return redirect('/cervezas')


@login_required
def cervBorrar(request, id):
    #return HttpResponse('Cervezas Borrar id: {}'.format(id))
    cervDel = Cerveza.objects.get(pk=id)
    cervDel.delete()
    return redirect('/cervezas')

#endregion Cervezas

@login_required
def pedidos(request):
    return render(request, 'Pedidos/pedidos.html')


@login_required
def ingresos(request):
    return render(request, 'Pedidos/ingresos.html')
