from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import pergunta

# Cadastro do usuário
def cadastro(request):
    if request.method == 'POST':
        form = pergunta(request.POST)
        if form.is_valid():
            # Aqui você salva tudo na sessão
            request.session['dados_usuario'] = form.cleaned_data
            return redirect('login') 
    else:
        form = pergunta() 
    
    return render(request, 'cadastro.html', {'form': form})

# Pega as informações de cadastro e compara com as do login
def login(request):
    if request.method == 'POST':
        form = pergunta(request.POST)
        if form.is_valid():
            # Pegamos o pacote da sessão
            cadastro_salvo = request.session.get('dados_usuario')
            
            if cadastro_salvo:
                # CORREÇÃO: Usamos [] para acessar os dados do dicionário
                nome_digitado = form.cleaned_data['nome']
                nome_registrado = cadastro_salvo['nome']
                
                if nome_digitado == nome_registrado:
                    # CORREÇÃO: Usamos () para a função redirect
                    return redirect('bemvindo')
            
            return HttpResponse('ERRO: Usuário com esse login não encontrado')
    else:
        form = pergunta() # Exibe o formulário vazio no primeiro acesso
        
    return render(request, 'login.html', {'form': form})
        
# Redireciona para uma tela de boas vindas em html
def bem_vindo(request):
    return render(request, 'bemvindo.html')