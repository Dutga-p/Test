# Generated by Django 4.2.6 on 2023-10-16 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0009_inventariovehiculo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventariovehiculo',
            options={'verbose_name_plural': 'InventarioVehiculo'},
        ),
        migrations.AlterModelTable(
            name='inventariovehiculo',
            table='InvetarioVehiculo',
        ),
    ]
