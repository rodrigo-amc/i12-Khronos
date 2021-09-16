from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Importo formularios
from .forms import frProveedor, frCerveza

from .models import Pedido, Proveedor, Cerveza, Ingreso, Barril
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


#region Pedidos
@login_required
def pedidos(request):
    ctxPedidos = {
        'proveedores': Proveedor.objects.all(),
        'lstPedidos' : Pedido.objects.all()
    }
    
    return render(request, 'Pedidos/pedidosListado.html', ctxPedidos)



@login_required
def pedidosNuevo(request, idP):
    if request.method == "GET":
        id = idP
        ctxt = {
            'prv' : Proveedor.objects.get(pk=id)
        }
        return render(request, 'Pedidos/pedidosNuevo.html', ctxt)
    
    elif request.method == 'POST':
        usuario = request.user
        proveedor = Proveedor.objects.get(pk=idP)
        #cerevzas = proveedor.cerveza_set.all()
        
        #Creo objeto pedido Pedido
        pedido = Pedido()
        pedido.usuario = usuario
        pedido.proveedor = proveedor
        pedido.save()

        lstCerv = request.POST.getlist('lineasCerv')
        lstCant = request.POST.getlist('lineaCant')
        
        for i in range(len(lstCerv)):
            """ print(str(lstCerv[i])+" : "+str(lstCant[i]))
            print(" ") """

            pedido.cerveza.add(Cerveza.objects.get(pk=lstCerv[i]), through_defaults={'cantidad':lstCant[i]})

        return redirect('/pedidos')



@login_required
def pedidoBorrar(request, idPedido):
    pedido = Pedido.objects.get(pk=idPedido)
    if pedido.entregado:
        return HttpResponse("No se puede borrar un pedido entregado. no no no señor!")
    else:
        for linea in pedido.lineapedido_set.all():
            linea.delete()
        pedido.delete()
        return redirect('/pedidos')

@login_required
def ingresosListado(request):
    cntxt = {
        'pedidos' : Pedido.objects.all()
    }
    return render(request, 'Pedidos/ingresos.html', cntxt)



def crearIngreso(request, idPedido):
    """Procesa El Ingreso De Un Pedido"""

    # Pedido Seleccionado
    pedido = Pedido.objects.get(pk=idPedido)
    
    # Lineas Del Pedido Seleccionado
    lineas = pedido.lineapedido_set.all()

    # Lista Con los valores de los input de "Cantidad Recibida"
    lstCantRec = request.POST.getlist('recibido')

    # Lista con los valores de numero de Barril
    lstBarriles = request.POST.getlist('barriles')

    # Si la peticion es por GET muestra la grilla para indicar las cantidades
    # que se reciben
    if request.method == 'GET':
        
        ctxt = {
            'pedido' : pedido,
            'lineas': lineas
        }

        return render(request, 'Pedidos/pedidoTablaIngreso.html', ctxt)
    
    # Si la peticion es por POST y se reciben valores en la lista 'recibido'
    # muestra la pantalla para indicar el numero de barril
    # por cada cerveza recibida
    elif request.method == 'POST' and len(lstCantRec)!=0:
        
        lstCerv = []

        # En un rango de la longitud = a la cantidad de elementos en "lstCantRec"
        for i in range(len(lstCantRec)):
            # En un rango de la longitud = a cada uno de los elementos de "lstCantRec"
            for c in range(int(lstCantRec[i])):
                # Se agrega la i° (i definida en el primer 'for') linea de pedido
                # a la lista "lstCerv"
                lstCerv.append(lineas[i])

        contexto = {
            'lstCerv':lstCerv,
            # Envio las cantidades al siguiente template ya que
            # en ese no van a existir
            'cantidades': lstCantRec
            }
        
        return render(request, 'Pedidos/pedidoBarriles.html', contexto)


    # Si la peticion es por POST y se reciben valores en la lista 'barriles'
    # se crea la Recepcion, el Pedido cambia de estado a "recibido",
    # y se crean un barril por cada cantidad recibida.
    elif request.method == 'POST' and len(lstBarriles)!=0:
        #Creo Un Ingreso
        ingreso = Ingreso()

        #Cambia el estado del pedido a "Entregado"
        pedido.entregado = True

        # Relaciono el Ingreso con el Pedido
        ingreso.pedido = pedido

        # Asigno al ingreso el numero de remito
        ingreso.numeroRemito = int(request.POST.get('remito'))

        # Asigno al ingreso Fecha De Remito
        ingreso.fechaRemito = request.POST.get('fecha')

        # Guardo el ingreso 
        ingreso.save()

        # Recibo las cantidades ingresadas en el template en el
        # input "hidden"
        cantidades = request.POST.getlist('cant')

        # En esta lista se guardan lineas de pedido. Cada linea se guarda
        # tantas veces como la cantidad recibida indique. La uso para
        # instanciar un barril por cada linea en la lista.
        lineaBarril = []

        # Asigno a cada linea la cantidad recibida
        # Itero tantas veces como lineas tenga el pedido
        for i in range(len(lineas)):
            # A la i° linea le asigno el valor de la i° cantidad
            lineas[i].entregado = int(cantidades[i])

            # Calculo la cantidad del campo "pendiente" para cada linea
            lineas[i].pendiente = lineas[i].cantidad - lineas[i].entregado

            # Guardo los cambios
            lineas[i].save()
            
            # Agrego en la lista "lineaBarril" cada linea, tantas veces como lo
            # indique la cantidad entregada. Luego uso esa lista para instanciar
            # los barriles y asignarles el numero de barril de la
            # lista "lstBarriles".
            for x in range( lineas[i].entregado):
                lineaBarril.append(lineas[i])
                        
        for b in range(len(lineaBarril)):
            barril = Barril()
            barril.ingreso = ingreso
            barril.numBarril = lstBarriles[b]
            barril.save()

        #Guardo el pedido
        pedido.save()

        
        cntxBarriles = {
            'ingresos' : Ingreso.objects.all(),
        }
        return redirect('/listarIngresos')
            

    else:
        return HttpResponse('naditas')



def listIngresos(request):

    ingDict = {}
    ingresos = Ingreso.objects.all()

    for ing in ingresos:
        ingDict[ing]=[]
    
    for i in ingDict:
        lineas = i.pedido.lineapedido_set.all()
        for linea in lineas:
            for x in range(linea.entregado):
                ingDict[i].append(linea.cerveza)


    ingContext = {
        'ingresos' : ingDict
    }
    return render(request, 'Pedidos/ingresoListado.html', ingContext)
#endregion pedidos




