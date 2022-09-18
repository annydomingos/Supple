from django.shortcuts import render, HttpResponse, redirect
from .forms import MovimentacaoForm, LoginForm, PoupancaForm
from .models import  Movimentacao, Carteira, Poupanca
from django.contrib import messages
from django.contrib.auth import login, logout

from usuario.models import Usuario



# Create your views here.
def saldo(request):
    if request.user.is_authenticated:
        saldo_usuario = Carteira.objects.filter(usuario_id=request.user.id).first()
        print(saldo_usuario)
        lista_movi = Movimentacao.objects.filter(usuario_id=request.user.id).order_by('id')
        entradas = lista_movi.filter(tipo_movimentacao="Entrada")
        despesas = lista_movi.filter(tipo_movimentacao="Despesa")
        if lista_movi.count() > 0:
            entradas_usuario = 0
            entradas_usuario = sum([e.valor or 0 for e in entradas])
            despesas_usuario = sum([d.valor or 0 for d in despesas])
            saldo_usuario.saldo = entradas_usuario - despesas_usuario
            saldo_usuario.save()
            return saldo_usuario.saldo
        else:
            pass
    else:
        pass

def index(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
        movimentacao = Movimentacao.objects.all()
        carteira = Carteira.objects.filter(usuario=request.user).first()
        saldo_do_usuario = saldo(request)
        context = { 'movimentacao' : movimentacao, 'carteira' : carteira , "saldo_do_usuario" : saldo_do_usuario }
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
                tipo_movimentacao = form.cleaned_data['tipo_movimentacao'],
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
                user = Usuario.objects.filter(email=form.cleaned_data['username']).first()
                print(user)
                print(Usuario.objects.filter(email=form.cleaned_data['username']))
                if user:
                    if user.check_password(form.cleaned_data['password']):
                        messages.success(request, 'Logout realizado com sucesso')
                        login(request, user)
                        return redirect('pagina_inicial')
                    else:
                        messages.error(request, 'Usuário ou senha inválido')
                else:
                    messages.error(request, 'Usuário ou senha inválido')


    messages.error('Erro ao logar')
    return render(request, 'login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        #messages.sucess(request, 'Logout realizado com sucesso')
        return redirect('login')
#depois modificar para direcionar para página inicial, quando tiver uma

def extrato(request):
    if request.user.is_authenticated:
        lista_mov = Movimentacao.objects.filter(usuario=request.user).order_by('-data')
        saldo_do_usuario = saldo(request)
        context = {'lista_mov' : lista_mov, 'saldo_do_usuario' : saldo_do_usuario}
        return render(request, 'extrato.html', context)
    else:
        return redirect('login')


def pagina_inicial(request):
    if request.user.is_authenticated:
        saldo_do_usuario = saldo(request)
        context = {"saldo_do_usuario" : saldo_do_usuario }
        return render(request,'paginainicial.html', context)
    else:
        return redirect('login')

def poupanca(request):
    if request.user.is_authenticated:
        lista_poupanca = Poupanca.objects.filter(usuario=request.user).order_by('-id')
        context = {'lista_poupanca' : lista_poupanca}
        return render(request,'poupanca.html', context)
    else:
        return redirect('login')

def nova_poupanca(request):
    if request.user.is_authenticated:
        lista_poupanca = Poupanca.objects.filter(usuario=request.user).order_by('-id')
        context = {'lista_poupanca' : lista_poupanca}
        return render(request, "novapoupanca.html", context)
    else:
        return redirect('login')



def nova_poupanca_submit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PoupancaForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                try:
                    poup = Poupanca.objects.create(
                    nome_poupanca = form.cleaned_data['nome_poupanca'],
                    saldo_poupanca = form.cleaned_data['saldo_poupanca'],
                    )
                    poup.save()
                    messages.success(request, "Poupança criada com sucesso")
                    lista_poupanca = Poupanca.objects.order_by('-id')
                    context = {'lista_poupanca' : lista_poupanca}

                    return render(request,'novapoupanca.html', context)
                except:
                    messages.error(request,'Erro ao criar objeto')
                    return render(request,'novapoupanca.html')
            else:
                messages.error(request, form.errors)
                return render(request,'novapoupanca.html')
        else:
            return render(request, 'novapoupanca.html', {'poup' : poup})
    else:
        return redirect('login')


