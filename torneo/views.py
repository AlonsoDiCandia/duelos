from django.shortcuts import render
from .forms import AñadirJugador

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