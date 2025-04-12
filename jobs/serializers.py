from rest_framework import serializers
from .models import Vaga

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'
