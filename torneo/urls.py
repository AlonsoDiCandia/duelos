from . import views
from django.urls import path, include

urlpatterns = [
    path('anadir-jugador/', views.añadir_jugador, name="añadir_jugador"),
    path('ver/', views.ver_jugadores, name="ver_jugadores"),
]