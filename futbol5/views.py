from django.shortcuts import render
from django.http import HttpResponse

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

# Create your views here.