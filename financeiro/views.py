from logging import exception
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .forms import MovimentacaoForm
from .models import Movimentacao
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')


def login_submit(request):
    if request.method == 'POST':
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                messages.sucess(request, 'Login realizado com sucesso')
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Usuário ou senha inválido')
                return render(request, 'login.html')

    messages.error('Erro ao logar')


# @login_required(login_url='/login/')
def logout_user(request):
    #verificando se o usuário está logado, pois se não estiver logado não como fazer logout
    if request.user.is_authenticated:
        logout(request)
        return render(request,'login.html')
#depois modificar para direcionar para página inicial, quando tiver uma
