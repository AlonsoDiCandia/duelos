from django.db import models

# Create your models here.

class Jugador(models.Model):	
	name = models.CharField(max_length=250)
	duelos_jugados = models.IntegerField()
	victorias = models.IntegerField()
	derrotas = models.IntegerField()





