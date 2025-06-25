# En este archivo estarán las funciones para activar la cuenta del usuario y recuperar contraseña
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect

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
        return HttpResponse("Error al activar tu cuenta.")
