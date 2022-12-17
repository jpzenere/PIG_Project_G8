from django.db import models


# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return f"{self.nombre}"


class Jugador(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name="Email")
    dni = models.IntegerField(verbose_name="DNI")
    edad = models.IntegerField(verbose_name="Edad")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name="Equipo")

    class Meta:
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return f"DNI: {self.dni} - {self.apellido}, {self.nombre}"



class Cancha(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    localidad = models.CharField(max_length=50, verbose_name="Localidad")
    telefono = models.IntegerField(verbose_name="Teléfono")
    ubicacion = models.URLField(verbose_name="Ubicación")

    