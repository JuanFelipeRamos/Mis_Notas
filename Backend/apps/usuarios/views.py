from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Usuario
from .serializers import RegistroUsuarioSerializer, UsuarioSerializer

class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer

class ListUsuarioView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilUsuarioView(APIView):
    permission_classes = IsAuthenticated

    def get(self, request):
        usuario = request.user
        data = {
            "email": usuario.email,
            "username": usuario.username,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }
        return Response(data)
