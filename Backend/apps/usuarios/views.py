import requests
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import traceback
from rest_framework.views import APIView
from .models import Usuario
from .serializers import RegistroUsuarioSerializer, UsuarioSerializer
from .emails import send_email


class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer

class ListUsuarioView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PerfilUsuarioView(APIView):
    permission_classes = IsAuthenticated

    def get(self, request):
        usuario = request.user
        data = {
            "email": usuario.email,
            "username": usuario.username,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }
        return Response(data)


#---Función para obtener el email enviado, buscar ese usuario, pasar su ID a base64 y generarle un token ------------->
User = get_user_model()

def obtener_usuario(request):
    email_user = request.data.get('email')

    try:
        usuario = User.objects.get(email=email_user)
    except User.DoesNotExist:
        return None
    uid = urlsafe_base64_encode(force_bytes(usuario.pk))
    token = default_token_generator.make_token(usuario)

    return {
        'email_user': email_user,
        'first_name': usuario.first_name,
        'uid': uid,
        'token': token
    }
#--------------------------------------------------------------------------------------->

# Vista para enviar email de validación de correo ingresado por el usuario (al registrarse)
class MsgValidacionEmailView(APIView):
    def post(self, request):
        datos_usuario = obtener_usuario(request)

        if not datos_usuario:
            return Response({
                "error": "Usuario no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        verification_url = request.build_absolute_uri(
            reverse('activar-cuenta', kwargs={'uidb64': datos_usuario['uid'], 'token': datos_usuario['token']})
        )

        subject = "Verifica tu correo en Mis Tareas"
        html_content = f"""
        <h1>Hola {datos_usuario['first_name']},</h1>
        <p>Gracias por registrarte en Mis Tareas. Haz clic en el siguiente enlace para verificar tu correo y así poder iniciar sesión:</p>
        <a href="{verification_url}">Verificar correo</a>
        """

        try:
            resultado = send_email(datos_usuario['email_user'], subject, html_content)

            if "exitosamente" in resultado:
                return Response({
                    "message": resultado
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": resultado
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.RequestException as e:
            print("Excepción inesperada:")
            traceback.print_exc()
            return Response({
                "error": f"No se pudo enviar el correo: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Vista para enviar email de recuperación de contraseña
class MsgRecuperarPasswordView(APIView):
    def post(self, request):
        datos_usuario = obtener_usuario(request)

        if not datos_usuario:
            return Response({
                "error": "Usuario no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        verification_url = f"http://localhost:5173/addnewpwd?uidb64={datos_usuario['uid']}&token={datos_usuario['token']}"

        subject = "Cambia tu contraseña en Mis Tareas"
        html_content = f"""
        <h1>Hola {datos_usuario['first_name']},</h1>
        <p>Has solicitado recuperar tu contraseña. Haz clic en el siguiente enlace para ingresar una nueva contraseña:</p>
        <a href="{verification_url}">Ingresar nueva contraseña</a>
        <p><strong>NOTA:</strong> Si no fuiste tú quien solicitó esta acción, por favor ignora este mensaje.</p>
        """

        try:
            resultado = send_email(datos_usuario['email_user'], subject, html_content)

            if "exitosamente" in resultado:
                return Response({
                    "message": resultado
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": resultado
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.RequestException as e:
            print("Excepción inesperada")
            traceback.print_exc()
            return Response({
                "error": f"no se pudo enviar el correo: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
