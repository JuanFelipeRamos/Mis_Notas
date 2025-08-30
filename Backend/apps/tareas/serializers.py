from rest_framework import serializers
from .models import Grupo

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ["id", "name", "description"]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["creador"] = request.user
        return super().create(validated_data)
