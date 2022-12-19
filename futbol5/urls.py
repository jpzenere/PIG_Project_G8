from django.urls import path, re_path, include
from futbol5 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inscripciones/crearEquipo/', views.crear_equipo, name='crear_equipo'),
    path('inscripciones/crearJugador/', views.crear_jugador, name='crear_jugador'),
    path('inscripciones/crearCancha/', views.crear_cancha, name='crear_cancha'),
    # path('cuentas/login', views.futbol5_login, name='login'),
    # path('cuentas/logout/',
    #      auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('cuentas/registrarse', views.futbol5_registrarse, name='registrarse'),
    path('accounts/', include('django.contrib.auth.urls'))
]



