from django.db import models
from users.models import CustomUser
from companies.models import Empresa  # Certifique-se de que o modelo Empresa está no app correto

class Mensagem(models.Model):
    remetente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="mensagens_enviadas")
    destinatario = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="mensagens_recebidas")
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('não lida', 'Não Lida'), ('lida', 'Lida')], default='não lida')

    def __str__(self):
        return f"De {self.remetente.cpf} para {self.destinatario.cnpj}"  # Supondo que Empresa tenha um campo 'nome'
