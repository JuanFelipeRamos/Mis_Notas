from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GrupoViewSet, ListarGrupoView

router = DefaultRouter()

router.register(r"grupos", GrupoViewSet, basename="grupos")

urlpatterns = [
    path("", include(router.urls)),
    path("listar_grupos/", ListarGrupoView.as_view(), name="listar-grupos"),
]
