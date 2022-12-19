from django.shortcuts import render, redirect
from django.http import HttpResponse
from futbol5.models import *
from .forms import EquipoForm, JugadorForm, CanchaForm, RegistrarUsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm



def index(request):
    return render(request, "index.html")

def inscripciones(request):
    jugadores = Jugador.objects.all().order_by('id')
    return render(request, "inscripciones.html", {'jugadores': jugadores})

def equipos(request):
    equipos = Equipo.objects.all().order_by('id')
    return render(request, "equipos.html", {'equipos': equipos})

def fixture(request):
    return render(request, "fixture.html")

def canchas(request):
    return render(request, "canchas.html")

def crear_equipo(request):
    formEquipo = EquipoForm(request.POST or None)
    if formEquipo.is_valid():
        formEquipo.save()
        formEquipo = EquipoForm()
    context = {'formEquipo': formEquipo}
    return render(request, "crear_equipo.html", context)

def crear_jugador(request):
    formJugador = JugadorForm(request.POST or None)
    if formJugador.is_valid():
        formJugador.save()
        formJugador = JugadorForm()
    context = {'formJugador': formJugador}
    return render(request, "crear_jugador.html", context)

def crear_cancha(request):
    formCancha = CanchaForm(request.POST or None)
    if formCancha.is_valid():
        formCancha.save()
        formCancha = CanchaForm()
    context = {'formCancha': formCancha}
    return render(request, "crear_cancha.html", context)


# def futbol5_login(request):
#     if request.method == 'POST':
#         # AuthenticationForm_can_also_be_used__
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             form = login(request, user)
#             messages.success(request, f' Bienvenido/a {username} !!')
#             return redirect('index')
#         else:
#             messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    
#     form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form, 'title': 'Log in'})



def futbol5_registrarse(request):
     if request.method == 'POST':
         form = RegistrarUsuarioForm(request.POST)
         if form.is_valid():
             form.save()
             messages.success(
                 request, f'Tu cuenta fue creada con éxito! Ya te podes loguear en el sistema.')
             return redirect('login')
     else:
         form = RegistrarUsuarioForm()
     return render(request, 'registrarse.html', {'form': form, 'title': 'registrese aquí'})