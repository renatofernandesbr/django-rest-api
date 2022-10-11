from rest_framework import serializers

from cliente.models import Cliente
from cliente.validator import validate_cpf, validate_nome, validate_rg


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, attrs):
        errors = []

        validate_cpf(attrs['cpf'], errors)
        validate_nome(attrs['nome'], errors)
        validate_rg(attrs['rg'], errors)

        if errors:
            raise serializers.ValidationError({'errors': errors})

        return attrs
