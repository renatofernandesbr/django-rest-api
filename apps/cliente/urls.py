from cliente.views import ClientesViewSet

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet, basename='Clientes')

urlpatterns = [
    path('', include(router.urls))
]
