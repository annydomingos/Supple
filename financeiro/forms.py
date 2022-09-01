from django import forms
from .models import Movimentacao

class MovimentacaoModelForm(forms.ModelForm):

  class Meta:
    model = Movimentacao
    fields = ['valor','usuario', 'carteira', 'tipo_movimentacao']
