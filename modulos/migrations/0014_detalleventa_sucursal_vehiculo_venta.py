# Generated by Django 4.2.6 on 2023-10-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0013_ordentrabajo_preciototal_repuesto_fechafabriacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('detalleVentaId', models.AutoField(primary_key=True, serialize=False)),
                ('ventaId', models.PositiveBigIntegerField()),
                ('cantidad', models.PositiveIntegerField()),
                ('vehiculoId', models.PositiveIntegerField()),
                ('nombreVehiculo', models.CharField(max_length=100)),
                ('subtotal', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'DetalleVenta',
                'db_table': 'DetalleVenta',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('sucursalId', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField()),
                ('ciudad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Sucursal',
                'db_table': 'Sucursal',
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('vehiculoId', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('img', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('modelo', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Vehiculo',
                'db_table': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('ventaId', models.AutoField(primary_key=True, serialize=False)),
                ('idUsuario', models.PositiveIntegerField()),
                ('telefonoCliente', models.PositiveBigIntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('vendedor', models.CharField(max_length=100)),
                ('vendedorId', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Venta',
                'db_table': 'Venta',
            },
        ),
    ]
