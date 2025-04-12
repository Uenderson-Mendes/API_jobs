from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Tentando autenticar usuário: {username}")  # Depuração

        try:
            user = CustomUser.objects.get(email=username)  # Buscar usuário pelo e-mail
        except CustomUser.DoesNotExist:
            print("Usuário não encontrado pelo e-mail.")
            return None

        if user and user.check_password(password):
            print("Autenticação bem-sucedida!")
            return user

        print("Senha incorreta.")
        return None
