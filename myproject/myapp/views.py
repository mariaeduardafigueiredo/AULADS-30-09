from django.shortcuts import render, redirect
from myapp.models import Usuario


# Create your views here.
def listar_usuarios(request):
    values = Usuario.objects.all()
    nome = request.GET.get('nome')
    if nome:
        values = values.filter(nome__icontains=nome)
   
    return render(request, 'myapp/pages/listar.html',{"lista_usuarios":values})

def criar_usuarios(request):
    nome = None
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            Usuario.objects.create(nome=nome, idade=idade)
            
    return render(request, 'myapp/pages/cadastrar.html', {"ultimo_nome":nome})

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