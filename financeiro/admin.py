from django.contrib import admin
from .models import Movimentacao, Carteira, Responsavel, Poupanca

# Register your models here.


class MovimentacaoAdmin(admin.ModelAdmin):
  list_display = ('valor', 'usuario', 'carteira','tipo_movimentacao', 'descricao', 'data')


admin.site.register(Movimentacao, MovimentacaoAdmin)


class CarteiraAdmin(admin.ModelAdmin):
  list_display = ('usuario', 'saldo')



admin.site.register(Carteira, CarteiraAdmin)

class ResponsavelAdmin(admin.ModelAdmin):
  list_display = ('filho', 'responsavel', 'parentesco')

admin.site.register(Responsavel, ResponsavelAdmin)


class PoupancaAdmin(admin.ModelAdmin):
  list_display = ('nome_poupanca', 'saldo_poupanca')

admin.site.register(Poupanca, PoupancaAdmin)
