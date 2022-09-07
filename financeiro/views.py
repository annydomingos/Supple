import email
from logging import exception
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .forms import Descricao_gastoForm, MovimentacaoForm, LoginForm
from .models import Descricao_gasto, Movimentacao
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from usuario.models import Usuario



# Create your views here.
def index(request):
    movimentacao = Movimentacao.objects.all()
    context = { movimentacao : 'movimentacao' }
    return render(request, 'index.html', context)

def index_submit(request):
    if request.method == 'POST':
        print(request.POST)
        form = MovimentacaoForm(request.POST, request.FILES)
        form1 = Descricao_gastoForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid() and form1.is_valid():
            try:
                mov = Movimentacao.objects.create(
                valor = form.cleaned_data['valor'],
                usuario_id = form.cleaned_data['usuario'],
                carteira_id = form.cleaned_data['carteira'],
                # tipo_movimentacao = form.cleaned_data['tipo_movimentacao'],
                )
                mov.save()
                desc = Descricao_gasto.objects.create(
                    descricao_gasto = form1.cleaned_data['descricao_gasto']
                )
                desc.save()
                print(desc)
                messages.success(request, 'Movimentação adicionada com sucesso')
                return redirect('index')
            except Exception as e:
                print(e)
                # print(form.cleaned_data['tipo_movimentacao'])
                messages.error(request,form.errors)
                return redirect('/')
        else:
            messages.error(request, form.errors)
            messages.error(request, form1.errors)
            # print(form.errors)
    return redirect('/')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')


def login_submit(request):
    if request.method == 'POST':

        if request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
            # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                user = Usuario.objects.filter(email=form.cleaned_data['username']).first()
                print(user)
                print(Usuario.objects.filter(email=form.cleaned_data['username']))
                if user:
                    if user.check_password(form.cleaned_data['password']):

                        messages.success(request, 'Login realizado com sucesso')
                        login(request, user)
                        return redirect('/')
                    else:
                        messages.error(request, 'Usuário ou senha inválido')


                else:
                    messages.error(request, 'Usuário ou senha inválido')


    messages.error('Erro ao logar')
    return render(request, 'login.html')


# @login_required(login_url='/login/')
def logout_user(request):
    #verificando se o usuário está logado, pois se não estiver logado não como fazer logout
    if request.user.is_authenticated:
        logout(request)
        return render(request,'login.html')
#depois modificar para direcionar para página inicial, quando tiver uma
