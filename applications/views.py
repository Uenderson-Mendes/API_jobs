from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Candidatura
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Candidatura.objects.all()
    serializer_class = ApplicationSerializer
