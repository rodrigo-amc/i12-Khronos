#region URLS APP
# Cuando se crea la aplicación el framework no crea este archivo.
# Hay que crearlo a mano.
# La idea es que cada aplicación tenga su propio archivo de urls,
# para que esta sea lo mas independiente posible del proyecto y
# pueda ser reutilizada en otros proyectos.
# Este archivo de urls debe ser importado en /Proyecto/urls.py
# 
#endregion

#importo "path" desde django
from django.urls import path

#Importo el archivo de vistas de la aplicación
from Pedidos import views

#creo la lista con las urls en las que van a estar TODAS las urls
#de la aplicación "Pedidos"
urlpatterns = [
    path('', views.logIn, name='LogIn'),
    path('menu', views.menuPrincipal, name='Menu'),
    path('usuarios', views.usuarios, name='Usuarios'),
    path('proveedores', views.proveedores, name='Proveedores'),
    path('pedidos', views.pedidos, name="Pedidos"),
    path('ingresos', views.ingresos, name='Ingresos'),
]

# Argumentos de path
# El primer argumento es la url
# El segundo argumento es la Vista (controlador) que procesa la petición
# El tercer argumento es el nombre por el cual se va a hacer referencia
#    desde los archivos html #