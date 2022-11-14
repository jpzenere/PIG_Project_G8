from django.urls import path
from futbol5 import views

urlpatterns = [
    path('inscripciones/jugadores', views.jugadores_tabla, name='jugadores_tabla'),
]



