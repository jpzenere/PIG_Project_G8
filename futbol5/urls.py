from django.urls import path
from futbol5 import views

urlpatterns = [
    path('inscripciones/crearEquipo/', views.crear_equipo, name='crear_equipo'),
    path('inscripciones/crearJugador/', views.crear_jugador, name='crear_jugador'),
    
]



