from django import forms
from .models import Equipo, Jugador, Cancha
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']