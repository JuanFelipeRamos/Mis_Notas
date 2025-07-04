# En este archivo estarán las funciones para activar la cuenta del usuario y cambiar contraseña
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status

# Función para activar la cuenta del usuario (para que pueda iniciar sesión)
User = get_user_model()

def activar_cuenta(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        usuario = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        usuario = None

    if usuario is not None and default_token_generator.check_token(usuario, token):
        usuario.is_active = True
        usuario.save()
        return HttpResponseRedirect("http://localhost:5173/")
    else:
        return HttpResponse("Error al activar tu cuenta.") # CAMBIAR!!!!


# Función para cambiar la contraseña del usuario
@api_view(['POST'])
def recuperar_pwd(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        usuario = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        usuario = None

    if usuario is not None and default_token_generator.check_token(usuario, token):
        new_password = request.data.get('password')
        usuario.set_password(new_password)
        usuario.save()

        return Response({
            "message": "contraseña recuperada con éxito."
        },status=status.HTTP_200_OK)
    else:
        return Response({
            "error": "El enlace no es válido o ha expirado."
        }, status=status.HTTP_400_BAD_REQUEST)
