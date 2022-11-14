from django.shortcuts import render
from django.http import HttpResponse
from futbol5.models import *


def index(request):
    return render(request, "index.html")

def inscripciones(request):
    return render(request, "inscripciones.html")

def equipos(request):
    return render(request, "equipos.html")

def fixture(request):
    return render(request, "fixture.html")

def canchas(request):
    return render(request, "canchas.html")

def jugadores_tabla(request):
    jugadores = Jugador.objects.all().order_by('id')
    return render(request, "jugadores_tabla.html", {'jugadores': jugadores})


# Create your views here.