#pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GrupoSerializer
from .models import Grupo

# Vista para crear grupos
class CrearGrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]


# Vista para listar grupos (del usuario autenticado)
class ListarGrupoView(ListAPIView):
    serializer_class = GrupoSerializer

    def get_queryset(self):
        user = self.request.user
        return Grupo.objects.filter(creador=user)
