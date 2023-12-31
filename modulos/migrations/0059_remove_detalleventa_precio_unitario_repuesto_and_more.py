# Generated by Django 4.2.5 on 2023-11-23 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0058_detalleventa_precio_unitario_repuesto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='precio_unitario_repuesto',
        ),
        migrations.RemoveField(
            model_name='detalleventa',
            name='precio_unitario_vehiculo',
        ),
        migrations.AlterField(
            model_name='venta',
            name='precioTotal',
            field=models.FloatField(blank=True, default=0.0, editable=False),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vendedor_id',
            field=models.ForeignKey(limit_choices_to={'rol': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.usuario'),
        ),
        migrations.AlterModelTable(
            name='detalleventa',
            table=None,
        ),
    ]
