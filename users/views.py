from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import viewsets
from .models import CustomUser

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Protege esta view
