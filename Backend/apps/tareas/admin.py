from django.contrib import admin
from .models import Grupo, Lista

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ("name", "creador", "creation_date")

@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ("name", "creador", "nombre_grupo", "creation_date")

    def nombre_grupo(self, obj):
        return obj.grupo.name if obj.grupo else "-"
    nombre_grupo.short_description = "GRUPO"
