from django.urls import path
from .views import RegistroUsuarioView, ListUsuarioView, PerfilUsuarioView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuarios"),
    path("listar_usuarios/", ListUsuarioView.as_view(), name="listar-usuarios"),
    path("me", PerfilUsuarioView.as_view(), name="perfil-usuario"),
]
