

# Create your models here.
from django.db import models
from users.models import CustomUser
from jobs.models import Vaga

class Candidatura(models.Model):
    STATUS_CANDIDATURA = [
        ('pendente', 'Pendente'),
        ('analisando', 'Analisando'),
        ('entrevista', 'Entrevista'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]
    
    candidato = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CANDIDATURA, default='pendente')
    data_candidatura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.username} - {self.vaga.titulo}"
