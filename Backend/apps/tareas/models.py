from django.db import models
from apps.usuarios.models import Usuario

class Grupo(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=150, blank=True, null=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name, self.creador, self.creation_date}"

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"


class Lista(models.Model):
    name = models.CharField(max_length=41)
    description = models.TextField(max_length=100, blank=True, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name, self.creador}"

    class Meta:
        verbose_name = "Lista"
        verbose_name_plural = "Listas"


class Tarea(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=100, blank=True, null=True)
    estado = models.BooleanField(default=False)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name, self.creador}"

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
