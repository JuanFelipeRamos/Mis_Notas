from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import RegistroUsuarioSerializer, UsuarioSerializer

class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer

class ListUsuarioView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer