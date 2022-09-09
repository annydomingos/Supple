from email.policy import default
from django import forms
from .models import Movimentacao
from django.utils import timezone

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
  descricao = forms.CharField(max_length=255)
  data = forms.DateField(widget=forms.DateInput, initial=timezone.now)


class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(max_length=255)

class PoupancaForm(forms.Form):
  nome_poupanca = forms.CharField(max_length=40)
  saldo_poupanca = forms.DecimalField(decimal_places=2, max_digits=10, initial=0)


