#pylint: disable=no-member
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
    id_grupo = serializers.IntegerField(write_only=True)
    grupo = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Lista
        fields = ["id", "name", "description", "id_grupo", "grupo"]

    # para asignar la lista al grupo seleccionado
    def create(self, validated_data):
        id_grupo = validated_data.pop("id_grupo")
        grupo = Grupo.objects.get(id=id_grupo)
        validated_data["grupo"] = grupo
        return super().create(validated_data)
