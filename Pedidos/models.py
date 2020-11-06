from django.db import models

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

class Cerveza(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    proveedor = models.ManyToManyField(Proveedor)