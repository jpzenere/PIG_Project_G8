from django.shortcuts import render
from django.http import HttpResponse
from futbol5.models import *
from .forms import EquipoForm, JugadorForm, CanchaForm


def index(request):
    return render(request, "index.html")

def inscripciones(request):
    jugadores = Jugador.objects.all().order_by('id')
    return render(request, "inscripciones.html", {'jugadores': jugadores})

def equipos(request):
    return render(request, "equipos.html")

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




# Create your views here.