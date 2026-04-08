from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import pergunta

def cadastro(request):
    if request.method == 'POST':
        form = pergunta(request.POST)
        if form.is_valid():
            # TUDO AQUI DENTRO PRECISA DE UM TAB (4 espaços)
            request.session['dados_usuario'] = form.cleaned_data
            return redirect('login')
    else:
        form = pergunta()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = pergunta(request.POST)
        if form.is_valid():
            # Buscamos o que foi salvo no cadastro
            cadastro_salvo = request.session.get('dados_usuario')
            nome_digitado = form.cleaned_data['nome']

            if cadastro_salvo and nome_digitado == cadastro_salvo['nome']:
                # CRIAMOS O CRACHÁ: Agora o usuário está "logado" na sessão
                request.session['usuario_autenticado'] = True
                return redirect('bemvindo')
            else:
                return HttpResponse("Dados não conferem com o cadastro.")
    else:
        form = pergunta()
    return render(request, 'login.html', {'form': form})

def bem_vindo(request):
    # A TRAVA: Se não tiver o crachá na sessão, volta para o login
    if not request.session.get('usuario_autenticado'):
        return redirect('login')
    return render(request, 'bemvindo.html')