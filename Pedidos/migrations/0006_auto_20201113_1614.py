# Generated by Django 2.2 on 2020-11-13 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0005_auto_20201113_1554'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lineapedido',
            unique_together={('cerveza', 'pedido')},
        ),
    ]
