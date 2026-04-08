from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import pergunta
from django.contrib import messages
from polls.models import pergunta
from django.contrib.auth.decorators import login_required

# Create your views here

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        pergunta.objects.create(nome=nome, email=email, senha=senha)
        return redirect('login')
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        nome_digitado = request.POST.get('nome')
        senha_digitada = request.POST.get('senha')
        
        # TESTE 1: Ver se os dados estão chegando
        print(f"Tentativa de login: Nome={nome_digitado}, Senha={senha_digitada}")

        usuario = pergunta.objects.filter(nome=nome_digitado, senha=senha_digitada).first()

        if usuario:
            # TESTE 2: Ver se o usuário foi encontrado
            print(f"Usuário encontrado! ID: {usuario.id}")
            request.session['usuario_id'] = usuario.id
            return redirect('bemvindo')
        else:
            # TESTE 3: Se caiu aqui, os dados digitados não batem com o banco
            print("Erro: Usuário não encontrado no banco de dados.")
            return HttpResponse("Dados incorretos. Verifique o Admin.")

    return render(request, 'login.html')

def bem_vindo(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    return render(request, 'bemvindo.html')