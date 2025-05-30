from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
    username (obligatorio)
    first_name
    last_name
    email
    password
    is_staff
    is_superuser
    date_joined
    last_login
    """

    REQUIRED_FIELDS = ['email'] # Para que al crear un superusuario se pidan este campo

    def __str__(self):
        return f"{self.first_name, self.last_name}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
