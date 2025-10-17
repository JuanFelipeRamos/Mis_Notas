from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoViewSet, ListarGrupoView, ListaViewSet

router = DefaultRouter()

router.register(r"grupos", GrupoViewSet, basename="grupos")
router.register(r"listas", ListaViewSet, basename="listas")

urlpatterns = [
    path("", include(router.urls)),
    path("listar_grupos/", ListarGrupoView.as_view(), name="listar-grupos"),
]
