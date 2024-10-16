from django.shortcuts import render, redirect
from myapp.models import Usuario
from django.contrib.auth.decorators import login_required, permission_required


def cadastrar_usuario(request):
    # Lógica para cadastrar o usuário
    return render(request, 'cadastrar.html')

# Create your views here.
def listar_usuarios(request):
    values = Usuario.objects.all()
    nome = request.GET.get('nome')
    if nome:
        values = values.filter(nome__icontains=nome)
    return render(request, 'myapp/pages/listar.html',{"lista_usuarios":values})
@login_required(login_url='/login/')
def criar_usuarios(request):
    nome = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            Usuario.objects.create(nome=nome, idade=idade)
            
    return render(request, 'myapp/pages/cadastrar.html', {"ultimo_nome":nome})
@permission_required('myapp.remove_usuario', raise_exception=True)
def deletar_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(listar_usuarios)


def atualizar_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            usuario.nome = nome
            usuario.idade = idade
            usuario.save()
            return redirect(listar_usuarios)
        else:
            return render(request, 'myapp/pages/atualizar.html', {"item":usuario, "erro":True})
            
    return render(request, 'myapp/pages/atualizar.html', {"item":usuario})