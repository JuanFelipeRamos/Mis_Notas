from django.contrib import admin
from .models import Grupo, Lista

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ("name", "creador", "creation_date")

@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ("name", "creador", "grupo", "creation_date")
