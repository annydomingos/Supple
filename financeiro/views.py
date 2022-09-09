from django.shortcuts import render, HttpResponse, redirect
from .forms import MovimentacaoForm, LoginForm
from .models import  Movimentacao, Carteira
from django.contrib import messages
from django.contrib.auth import login, logout

from usuario.models import Usuario



# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        movimentacao = Movimentacao.objects.all()
        carteira = Carteira.objects.filter(usuario=request.user).first()
        context = { 'movimentacao' : movimentacao, 'carteira' : carteira }
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
                descricao = form.cleaned_data['descricao'],
                data = form.cleaned_data['data'],
                # tipo_movimentacao = form.cleaned_data['tipo_movimentacao'],
                )
                mov.save()
                messages.success(request, 'Movimentação adicionada com sucesso')
                return redirect('index')
            except Exception as e:
                print(e)
                # print(form.cleaned_data['tipo_movimentacao'])
                messages.error(request,form.errors)
                return redirect('/')
        else:
            messages.error(request, form.errors)

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


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'login.html')
#depois modificar para direcionar para página inicial, quando tiver uma

def extrato(request):
    if request.user.is_authenticated:
        lista_mov = Movimentacao.objects.order_by('-data')
        context = {'lista_mov' : lista_mov }
        return render(request, 'extrato.html', context)
    else:
        return redirect('login.html')


def pagina_inicial(request):
    if request.user.is_authenticated:
        return render(request,'paginainicial.html')
    else:
        return redirect('login.html')

def poupanca(request):
    if request.user.is_authenticated:
        return render(request,'poupanca.html')
    else:
        return redirect('login.html')

def saldo(request):
    pass
