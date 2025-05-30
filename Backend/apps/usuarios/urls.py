from django.urls import path, include
from .views import RegistroUsuarioView, ListUsuarioView

urlpatterns = [
    path("registro_usuarios/", RegistroUsuarioView.as_view(), name="registro-usuarios"),
    path("listar_usuarios/", ListUsuarioView.as_view(), name="listar-usuarios"),
]
