from rest_framework import serializers
from .models import Mensagem

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'
