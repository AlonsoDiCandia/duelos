from django.forms import ModelForm
from .models import Jugador

class AñadirJugador(ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'