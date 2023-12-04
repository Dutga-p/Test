# Generated by Django 4.2.5 on 2023-11-19 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0047_alter_rutas_descripcion_ruta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='vehiculo',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='vehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modulos.vehiculo'),
        ),
    ]
