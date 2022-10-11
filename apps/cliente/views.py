from cliente.models import Cliente
from cliente.serializer import ClienteSerializer

from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibe todos os clientes."""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nome', 'celular']
    filterset_fields = ['ativo']
    ordering_fields = ['id', 'nome']
    ordering = ['nome']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
