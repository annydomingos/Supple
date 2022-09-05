from logging import exception
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .forms import MovimentacaoForm
from .models import Movimentacao
from django.contrib import messages


# Create your views here.
def index(request):
    movimentacao = Movimentacao.objects.all()
    context = { movimentacao : 'movimentacao' }
    return render(request, 'index.html', context)

def index_submit(request):
    if request.method == 'POST':
        print(request.POST)
        form = MovimentacaoForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            try:
                mov = Movimentacao.objects.create(
                valor = form.cleaned_data['valor'],
                usuario_id = form.cleaned_data['usuario'],
                carteira_id = form.cleaned_data['carteira'],
                # tipo_movimentacao = form.cleaned_data['tipo_movimentacao'],
                )
                mov.save()
                messages.success(request, 'Movimentação adicionada com sucesso')
                return redirect('index')
            except Exception as e:
                print(e)
                print(form.cleaned_data['tipo_movimentacao'])
                messages.error(request, 'Erro ao salvar movimentação')
                return redirect('/')
        else:
            messages.error(request, "Movimentação inválida")
            # print(form.errors)
    return redirect('/')


#def test_bootstrap(request):
    # if request.method == 'GET':
    #     form1 = MovimentacaoModelForm()
    #     return render(request,'test_bootstrap.html')

    if request.method == 'POST':
        form1 = MovimentacaoForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Movimentação adicionada com sucesso')
            form1 = MovimentacaoForm()
        else:
            messages.error(request, 'Dados inválidos')
            return render(request, 'test_bootstrap.html ')
    else:
        form1 = MovimentacaoForm()
    context = { form1 : "form1"}
    print(form1)
    return render(request, 'test_bootstrap.html', context)

