from django.contrib import admin
from django.contrib.auth.admin import User
from .models import Cerveza

# Register your models here.
admin.site.register(Cerveza)
#admin.site.register(Pedido)
#admin.site.register(LineaPedido)
