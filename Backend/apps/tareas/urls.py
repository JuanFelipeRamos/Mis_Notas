from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrearGrupoViewSet

router = DefaultRouter()

router.register(r"crear_grupo", CrearGrupoViewSet, basename="Crear-grupo")

urlpatterns = [
    path("", include(router.urls)),
]
