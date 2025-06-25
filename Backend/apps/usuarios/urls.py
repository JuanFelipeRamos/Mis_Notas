from django.urls import path
from .views import RegistroUsuarioView, ListUsuarioView, PerfilUsuarioView, MsgValidacionEmailView
from .users import activar_cuenta

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuarios"),
    path("listar_usuarios/", ListUsuarioView.as_view(), name="listar-usuarios"),
    path("me/", PerfilUsuarioView.as_view(), name="perfil-usuario"),

    # Para envío de correos electrónicos
    path("msg_validar_email/", MsgValidacionEmailView.as_view(), name="mensage-validar-email"),

    # Para activar la cuenta del usuario
    path("activar_cuenta/<uidb64>/<token>/", activar_cuenta, name="activar-cuenta"),
]
