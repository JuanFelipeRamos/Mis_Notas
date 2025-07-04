from django.urls import path
from .views import RegistroUsuarioView, ListUsuarioView, PerfilUsuarioView, MsgValidacionEmailView, MsgRecuperarPasswordView
from .users import activar_cuenta, recuperar_pwd

urlpatterns = [
    path("registro/", RegistroUsuarioView.as_view(), name="registro-usuarios"),
    path("listar_usuarios/", ListUsuarioView.as_view(), name="listar-usuarios"),
    path("me/", PerfilUsuarioView.as_view(), name="perfil-usuario"),

    # Para envío de emails sobre activar cuenta
    path("msg_validar_email/", MsgValidacionEmailView.as_view(), name="mensage-validar-email"),

    # Para envío de emails sobre recuperar contraseña
    path("msg_recuperar_pwd/", MsgRecuperarPasswordView.as_view(), name="mensage-recuperar-password"),

    # Para activar la cuenta del usuario
    path("activar_cuenta/<uidb64>/<token>/", activar_cuenta, name="activar-cuenta"),

    # Para recuperar contraseña del usuario
    path("recuperar_pwd/<uidb64>/<token>/", recuperar_pwd, name="recuperar-password"),
]
