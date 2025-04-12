from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Mensagem
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MessageSerializer
