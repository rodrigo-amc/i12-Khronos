from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

# Imoporto el modelo "user" para usarlo en la subclase "Meta" de fr_CrearUsuario
from django.contrib.auth.models import User


class fr_CrearUsuario(UserCreationForm):
    """
    Esta clase representa un formulario para crear Usuarios
    basado en el modelo de usuarios que provee Django.
    """
    class Meta:
        """
        En esta clase se definen los campos que se van a mostrar
        en el formulario. Si no se indica ninguno, solo se
        muestran 'usuario' y 'contraseña'.
        """
        #Le indico con que modelo voy a trabajar
        model = User

        #Le indico que campos debe mostrar el formulario
        fields = [
            'username',
            'password1',
            'password2',
            'is_superuser',
        ]