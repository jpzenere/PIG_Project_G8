from django import forms
from .models import Equipo, Jugador, Cancha

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'nombre'
        ]

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            'nombre',
            'apellido',
            'email',
            'dni',
            'edad',
            'foto_perfil',
            'equipo'
        ]

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = [
            'nombre',
            'direccion',
            'localidad',
            'telefono',
            'ubicacion'
        ]