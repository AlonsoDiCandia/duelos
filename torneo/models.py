from django.db import models

# Create your models here.

class Jugador(models.Model):	
	nombre = models.CharField(max_length=250)
	duelos_jugados = models.IntegerField(default=0)
	victorias = models.IntegerField(default=0)
	derrotas = models.IntegerField(default=0)
