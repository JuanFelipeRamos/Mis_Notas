from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrearGrupoViewSet, ListarGrupoView

router = DefaultRouter()

router.register(r"crear_grupo", CrearGrupoViewSet, basename="Crear-grupo")

urlpatterns = [
    path("", include(router.urls)),
    path("listar_grupos/", ListarGrupoView.as_view(), name="listar-grupos"),
]
