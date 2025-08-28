from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import GrupoSerializer
from .models import Grupo

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = [IsAuthenticated]
