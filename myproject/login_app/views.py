from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Criar usuários
def criar_usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if all([nome, sobrenome, username, email, senha]):
            # Cria o usuário
            User.objects.create_user(username=username,
                                     password=senha,
                                     email=email,
                                     first_name=nome,
                                     last_name=sobrenome)
    return render(request, 'login_app/pages/cadastrar.html')

# Função para login
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        if username and senha:
            user = authenticate(username=username, password=senha)
            if user:
                login(request, user)
                return redirect('listar_usuarios')
            mensagem = 'Usuário ou senha inválidos'
            return render(request, 'login_app/pages/login.html', {'mensagem': mensagem})
    return render(request, 'login_app/pages/login.html')

# Função para logout (com indentação corrigida)
def logout_usuario(request):
    logout(request)
    return redirect(login_usuario)