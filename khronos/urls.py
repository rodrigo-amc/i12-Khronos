"""khronos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Importo las vistas de la aplicacion "Pedidos"
from Pedidos import views

#Acá se especifican las urls
urlpatterns = [
    path('admin/', admin.site.urls),

    #Rutas De La Aplicacion "Pedidos"
    path('', views.logIn, name='LogIn'),
    path('menu', views.menuPrincipal, name='Menu'),
    path('usuarios', views.usuarios, name='Usuarios'),
    path('proveedores', views.proveedores, name='Proveedores'),
    path('pedidos', views.pedidos, name="Pedidos"),
    path('ingresos', views.ingresos, name='Ingresos'),
]
