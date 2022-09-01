from django.shortcuts import render, HttpResponse, redirect
from financeiro.forms import MovimentacaoModelForm
from .models import Movimentacao
from django.contrib import messages


# Create your views here.
def index(request):
    movimentacao = Movimentacao.objects.all()
    context = { movimentacao : 'movimentacao' }
    return render(request, 'index.html', context)

def index_submit(request):
    if request.method == 'POST':
     form = MovimentacaoModelForm(request.POST, request.FILES)
     print(form.is_valid())
     if form.is_valid():
        form.save()
        return redirect('index')
     else:
        raise NameError('Método inválido')
    else:
        raise NameError('Operação inválida')
