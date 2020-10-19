from django.urls import path
from Usuarios import views

urlpatterns = [
    path('', views.logIn, name='LogIn'),

    #gestión de usuarios
    path('usuarios/', views.usuarios, name='usuarios'),
]