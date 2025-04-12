from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Empresa
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = CompanySerializer
