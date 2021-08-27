from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
#region Comentarios
# Las clases dentro de este modulo representan los modelos.
# Todos los modelos deben heredar de "models.Model". Esto
# le permite acceder a las funcionalidades del framework.

# Al crear las clases, si no se indica un campo "id", django crea automáticamente
# un campo "id", entero, autoincrement, primaryKey, etc...#

# 
# Una vez creados los modelos se ejecuta el comando
# "python manage.py makemigrations". Esto crea el
# archivo de migraciones en la carpeta "migrations"
# 
# Luego ejecutar "python manage.py migrate"
# Esto hace que el framework cree las tablas
# en la base de datos
#endregion

class Proveedor(models.Model):
    nombre      = models.CharField(max_length=(200), unique=True)
    domicilio   = models.CharField(max_length=(200))
    telefono    = models.CharField(max_length=(50))
    email       = models.EmailField()

    def __str__(self):
        return self.nombre



class Cerveza(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    proveedor = models.ManyToManyField(Proveedor)

    def __str__(self):
        return self.nombre


#region Modelos con relación ManyToMany
class Pedido(models.Model):
    fecha = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING)
    cerveza = models.ManyToManyField(Cerveza, through='LineaPedido')
    fechaEntrega = models.DateField(blank=True, null=True)
    entregado = models.BooleanField(default=False)


class LineaPedido(models.Model):
    cantidad = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    cerveza = models.ForeignKey(Cerveza, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#endregion