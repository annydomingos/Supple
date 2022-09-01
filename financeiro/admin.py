from django.contrib import admin
from .models import Movimentacao, Carteira, Responsavel, Descricao_gasto

# Register your models here.


class MovimentacaoAdmin(admin.ModelAdmin):
  list_display = ('valor', 'usuario', 'carteira','tipo_movimentacao')


admin.site.register(Movimentacao, MovimentacaoAdmin)


class CarteiraAdmin(admin.ModelAdmin):
  list_display = ('usuario', 'saldo')



admin.site.register(Carteira, CarteiraAdmin)

class ResponsavelAdmin(admin.ModelAdmin):
  list_display = ('filho', 'responsavel', 'parentesco')



admin.site.register(Responsavel, ResponsavelAdmin)

class Descricao_gastoAdmin(admin.ModelAdmin):
  list_display = ('valor', 'descricao', 'usuario', 'carteira')

admin.site.register(Descricao_gasto, Descricao_gastoAdmin)
