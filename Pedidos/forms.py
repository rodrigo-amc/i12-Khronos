from django.forms import ModelForm
from .models import Proveedor

# Ver Usuarios/forms.py

# Este formulario lo importo en "views.py" para instanciarlo
# y pasárselo en el context al controlador que renderiza
# el template de Proveedores. De ese modo puedo mostrar
# el formulario para crear proveedores.
class frProveedor(ModelForm):
    class Meta:
        model = Proveedor

        fields = '__all__'