# Generated by Django 3.2 on 2022-12-15 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('ubicacion', models.URLField(verbose_name='Ubicación')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbol5.equipo', verbose_name='Equipo')),
            ],
        ),
    ]