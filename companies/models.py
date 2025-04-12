# Create your models here.
from django.db import models
from users.models import CustomUser

class Empresa(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    localizacao = models.CharField(max_length=855)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    rua = models.CharField(max_length=855)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    descricao_empresa = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_fantasia
