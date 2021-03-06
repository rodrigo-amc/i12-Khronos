# Generated by Django 2.2 on 2020-11-24 23:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0004_cerveza'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name=django.core.validators.MinValueValidator(1, 'Valor Mínimo = 1'))),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pedidos.Cerveza')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('lineaPedido', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pedidos.LineaPedido')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pedidos.Proveedor')),
            ],
        ),
    ]
