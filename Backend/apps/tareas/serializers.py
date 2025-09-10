from rest_framework import serializers
from .models import Grupo, Lista

# clase base con la función para asignar el usuario
class BaseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["creador"] = request.user
        return super().create(validated_data)


# Serializer para grupos
class GrupoSerializer(BaseSerializer):
    class Meta:
        model = Grupo
        fields = ["id", "name", "description"]


# Serializer para listas
class ListaSerializer(BaseSerializer):
    class Meta:
        model = Lista
        fields = ["id", "name", "description"]
