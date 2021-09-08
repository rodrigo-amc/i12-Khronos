# Generated by Django 2.2 on 2021-08-26 23:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pedidos', '0010_auto_20210826_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.Cerveza')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('fechaEntrega', models.DateField(auto_now=True)),
                ('entregado', models.BooleanField(default=False)),
                ('cerveza', models.ManyToManyField(through='Pedidos.LineaPedido', to='Pedidos.Cerveza')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pedidos.Proveedor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lineapedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.Pedido'),
        ),
    ]