from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

class Meta:
    permissions = (
        ("remove_usuario", "Pode remover usúario"),
    )
    def __str__(self):
        return f"Usuario: {self.nome}, Idade: {self.idade}"
    

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.CharField(max_length=50)
    data_final = models.DateField()

    alunos = models.ForeignKey(Usuario, on_delete=models.CASCADE)