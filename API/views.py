from django.shortcuts import render
from rest_framework import generics
from .models import Receta
from .serializers import RecetaSerializers

class RecetaViewSet(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializers
    
