from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import re
from django.core.exceptions import ValidationError

# Gerenciador de Usuário Personalizado
class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Cria e retorna um usuário com e-mail e nome completo.
        """
        if not email:
            raise ValueError('O E-mail deve ser definido')

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        """
        Cria e retorna um superusuário com e-mail e nome completo.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, full_name, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Remove o campo username padrão do Django
    email = models.EmailField(unique=True, verbose_name="E-mail")  # E-mail como identificador único
    full_name = models.CharField(max_length=255, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF", blank=True, null=True)  # CPF opcional

    # Definir e-mail como campo único para login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()  # Usando o gerenciador customizado

    groups = models.ManyToManyField(Group, related_name="customuser_groups", verbose_name="Grupos")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    gender = models.CharField(max_length=50, null=True, blank=True, verbose_name="Gênero")
    address_city = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")
    address_state = models.CharField(max_length=100, null=True, blank=True, verbose_name="Estado")
    address_country = models.CharField(max_length=100, null=True, blank=True, verbose_name="País")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    linkedin_profile = models.URLField(null=True, blank=True, verbose_name="Perfil LinkedIn")

    academic_formation = models.TextField(null=True, blank=True, verbose_name="Grau de Formação")
    institution = models.CharField(max_length=255, null=True, blank=True, verbose_name="Instituição")
    course = models.CharField(max_length=255, null=True, blank=True, verbose_name="Curso")
    graduation_year = models.IntegerField(null=True, blank=True, verbose_name="Ano de Conclusão")

    previous_position = models.CharField(max_length=255, null=True, blank=True, verbose_name="Posição Anterior")
    company_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome da Empresa")
    work_period_start = models.DateField(null=True, blank=True, verbose_name="Início do Período de Trabalho")
    work_period_end = models.DateField(null=True, blank=True, verbose_name="Fim do Período de Trabalho")
    main_responsibilities = models.TextField(null=True, blank=True, verbose_name="Principais Responsabilidades")

    technical_skills = models.TextField(null=True, blank=True, verbose_name="Habilidades Técnicas")
    interpersonal_skills = models.TextField(null=True, blank=True, verbose_name="Habilidades Interpessoais")

    area_of_interest = models.CharField(max_length=255, null=True, blank=True, verbose_name="Área de Interesse")
    desired_contract_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tipo de Contrato Desejado")
    professional_summary = models.TextField(null=True, blank=True, verbose_name="Resumo Profissional")

    relevant_projects = models.TextField(null=True, blank=True, verbose_name="Projetos Relevantes")
    languages = models.TextField(null=True, blank=True, verbose_name="Idiomas")

    curriculum_attachment = models.FileField(upload_to='curriculums/', null=True, blank=True, verbose_name="Anexo do Currículo")

    def clean_cpf(self):
        # Verifica se o CPF contém apenas números e está no formato correto
        if self.cpf and not re.match(r'^\d{11}$', self.cpf):
            raise ValidationError("O CPF deve conter apenas números e ter exatamente 11 caracteres.")
        return self.cpf

    def assign_group(self):
        if self.email and "empresa" in self.email:
            group, _ = Group.objects.get_or_create(name="Empresas")
        else:
            group, _ = Group.objects.get_or_create(name="Empregados")

        self.groups.set([group])
        self.user_permissions.set(group.permissions.all())

    def save(self, *args, **kwargs):
        """Salva o usuário sem redefinir o grupo toda vez."""
        super().save(*args, **kwargs)

@receiver(post_save, sender=CustomUser)
def add_user_to_default_group(sender, instance, created, **kwargs):
    """Atribui o grupo APENAS quando um usuário é criado pela primeira vez."""
    if created:
        instance.assign_group()
