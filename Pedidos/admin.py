from django.contrib import admin
from django.contrib.auth.admin import User
from .models import Cerveza, Pedido, LineaPedido

# Register your models here.
admin.site.register(Cerveza)
admin.site.register(Pedido)
admin.site.register(LineaPedido)
