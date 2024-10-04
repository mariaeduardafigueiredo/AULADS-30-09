from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    username = models.CharField(max_length=100, unique=True)  # Nome de usuário único
    senha = models.CharField(max_length=100)  # Para armazenar a senha (use hash no futuro)

    def __str__(self):
        return self.nome


