# Generated by Django 2.2 on 2021-08-27 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0011_auto_20210826_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='fechaEntrega',
        ),
    ]
