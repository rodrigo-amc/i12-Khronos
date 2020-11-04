from django.urls import path
from Usuarios import views

urlpatterns = [
    path('', views.logIn, name='LogIn'),

    #gestión de usuarios
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarioNuevo', views.usuarioNuevo, name='usuarioNuevo'),

    # Esta ruta recibe el id del usuario por url y se lo envía el controlador "usuarioEditar".
    # El id del usuario se obtiene en el botón de editar en "usuarios.html"
    path('usuarioEditar/<int:id>', views.usuarioEditar, name='usuarioEditar'),

    path('usuarioBorrar/<int:id>', views.usuarioBorrar, name='usuarioBorrar'),
]