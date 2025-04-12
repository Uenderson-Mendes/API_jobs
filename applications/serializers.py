from rest_framework import serializers
from .models import Candidatura

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = '__all__'
