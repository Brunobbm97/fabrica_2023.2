from django.forms import ModelForm
from .models import Piloto


class PilotoForm(ModelForm):

    class Meta:
        model = Piloto
        fields = ['nome', 'num_carro', 'equipe', 'idade']
