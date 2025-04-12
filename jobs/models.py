from django.db import models

# Create your models here.
from django.db import models
from companies.models import Empresa

class Vaga(models.Model):
    TIPO_CONTRATO = [
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('Freelancer', 'Freelancer'),
        ('Temporário', 'Temporário'),
    ]
    
    MODELO_TRABALHO = [
        ('remoto', 'Remoto'),
        ('hibrido', 'Híbrido'),
        ('presencial', 'Presencial'),
    ]

    RAMOS_CHOICES = [
        ('tecnologia', 'Tecnologia'),
        ('suporte', 'Suporte'),
        ('administrativo', 'Administrativo'),
        ('saude', 'Saúde'),
        ('educacao', 'Educação'),
        ('financeiro', 'Financeiro'),
        ('engenharia', 'Engenharia'),
        ('marketing', 'Marketing'),
        ('vendas', 'Vendas'),
        ('juridico', 'Jurídico'),
        ('recursos_humanos', 'Recursos Humanos'),
        ('logistica', 'Logística'),
        ('administracao', 'Administração'),
        ('comunicacao', 'Comunicação'),
        ('arte_design', 'Arte e Design'),
        ('turismo', 'Turismo'),
        ('agropecuaria', 'Agropecuária'),
        ('construcao_civil', 'Construção Civil'),
        ('transporte', 'Transporte'),
        ('telecomunicacoes', 'Telecomunicações'),
        ('energia', 'Energia'),
        ('alimentacao', 'Alimentação'),
        ('agronegocio', 'Agronegócio'),
        ('outros', 'Outros'),
    ]
    FORMACAO_ACADEMICA_CHOICES = [
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('tecnico', 'Técnico'),
        ('graduacao', 'Graduação'),
        ('pos_graduacao', 'Pós-Graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
        ('outros', 'Outros'),
    ]
    
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    ramo = models.CharField(max_length=50, choices=RAMOS_CHOICES, default='ESCOLHA')
    formacao_academica = models.CharField(max_length=20, choices=FORMACAO_ACADEMICA_CHOICES, default='outros')
    tipo_contrato = models.CharField(max_length=15, choices=TIPO_CONTRATO)
    modelo_trabalho = models.CharField(max_length=15, choices=MODELO_TRABALHO, default='presencial')
    descricao = models.TextField()
    requisitos = models.TextField()
    diferenciais = models.TextField()
    responsabilidades = models.TextField()
    beneficios = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    salario = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Faixa Salarial",
        help_text="Informe a faixa salarial no formato: '1200 - 2000'"
    )

    def save(self, *args, **kwargs):
        if not self.salario.startswith('$'):
            self.salario = f'$ {self.salario}'
        if '.' in self.salario:
            self.salario = self.salario.replace(',', '')
        if self.salario.replace('$', '').replace(' ', '').isdigit():
            self.salario = f"$ {int(self.salario.replace('$', '').replace(' ', '')):,.2f} Reais"
        super().save(*args, **kwargs)
        super().save(*args, **kwargs)
    status = models.CharField(max_length=10, choices=[('ativa', 'Ativa'), ('encerrada', 'Encerrada')], default='ativa')

    def __str__(self):
        return self.titulo
