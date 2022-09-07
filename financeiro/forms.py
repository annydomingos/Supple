from django import forms
from .models import Movimentacao, Descricao_gasto

class MovimentacaoForm(forms.Form):
  # TIPO_DESPESA = 'DESPESA'
  # TIPO_ENTRADA = 'ENTRADA'

  # TIPO_MOVIMENTACAO_CHOICES = (
  #   (TIPO_DESPESA, 'despesa'),
  #   (TIPO_ENTRADA, 'entrada'),
  # )
  # tipo_movimentacao = widget=forms.Select(choices=TIPO_MOVIMENTACAO_CHOICES)
  carteira = forms.IntegerField()
  usuario = forms.IntegerField()
  valor = forms.DecimalField(decimal_places=2, max_digits=10)

class Descricao_gastoForm(forms.Form):
  descricao_gasto = forms.CharField(max_length=127)

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(max_length=255)


