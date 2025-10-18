#pylint: disable=no-member
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import GrupoSerializer, ListaSerializer
from .models import Grupo, Lista

# Vista para crear, listar, editar y eliminar grupos
class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]


# Vista para listar grupos (del usuario autenticado)
class ListarGrupoView(ListAPIView):
    serializer_class = GrupoSerializer

    def get_queryset(self):
        user = self.request.user
        return Grupo.objects.filter(creador=user)


# Vista para crear, listar, editar y eliminar listas
class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [IsAuthenticated]


# Vista para listar listas (del grupo seleccionado)
class ListarListaView(ListAPIView):
    serializer_class = ListaSerializer

    def get_queryset(self):
        id_grupo = self.request.query_params.get("id_grupo")

        if not id_grupo:
            return Lista.objects.none()

        try:
            grupo_seleccionado = Grupo.objects.get(pk=id_grupo)
        except Grupo.DoesNotExist:
            return Lista.objects.none()

        return Lista.objects.filter(grupo=grupo_seleccionado)
