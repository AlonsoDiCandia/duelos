from django.shortcuts import render
from .forms import AñadirJugador
from .models import Jugador

# Create your views here.

def añadir_jugador(request):
	if request.method == 'POST':
		form = AñadirJugador(request.POST)
		if form.is_valid():
			form.save()
			form = AñadirJugador()
		else:
			print("NO") #change this!
	else:
		form = AñadirJugador()

	return render(request, "torneo/anadir_jugador.html", {'new_menu': form})

def ver_jugadores(request):
	jugadores = Jugador.objects.all()

	return render(request, "torneo/ver.html", {"jugadores": jugadores})