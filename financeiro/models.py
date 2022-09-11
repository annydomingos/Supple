from django.utils import timezone
from django.db import models
from usuario.models import Usuario
# Create your models here.

class Movimentacao(models.Model):
  TIPO_DESPESA = 'DESPESA'
  TIPO_ENTRADA = 'ENTRADA'

  TIPO_MOVIMENTACAO_CHOICES = (
    (TIPO_DESPESA, 'despesa'),
    (TIPO_ENTRADA, 'entrada'),
  )
  valor = models.DecimalField('Valor', blank=False, null=False, decimal_places=2, max_digits=10)
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  carteira = models.ForeignKey("Carteira", verbose_name='Carteira', on_delete=models.CASCADE)
  tipo_movimentacao = models.CharField(max_length=7, choices=TIPO_MOVIMENTACAO_CHOICES, default='Entrada')
  descricao = models.CharField('Descrição', max_length=255, blank=True, null=True)
  data = models.DateField('Data', default=timezone.now())

  def __str__(self) :
    return str(self.valor)

class Carteira(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  saldo = models.DecimalField('Saldo', decimal_places=2, max_digits=10, default=0)

  def __str__(self):
    return str(self.id)


class Responsavel(models.Model):
  filho = models.ForeignKey(Usuario, verbose_name='Filho', on_delete=models.CASCADE)
  responsavel = models.CharField('Responsável', max_length=50)
  parentesco = models.CharField('Parentesco', max_length=50)

  def __str__(self):
    return str(self.filho)

class Poupanca(models.Model):
  nome_poupanca = models.CharField('Descrição', max_length=40)
  saldo_poupanca = models.DecimalField('Saldo', decimal_places=2, max_digits=10, default=0)



