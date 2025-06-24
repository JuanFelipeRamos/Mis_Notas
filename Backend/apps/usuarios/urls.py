from django.urls import path
from .views import RegistroUsuarioView, ListUsuarioView, PerfilUsuarioView, MsgValidacionEmailView

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuarios"),
    path("listar_usuarios/", ListUsuarioView.as_view(), name="listar-usuarios"),
    path("me/", PerfilUsuarioView.as_view(), name="perfil-usuario"),

    # Para envío de correos electrónicos
    path("msg_validar_email/", MsgValidacionEmailView.as_view(), name="mensage-validar-email"),
]
