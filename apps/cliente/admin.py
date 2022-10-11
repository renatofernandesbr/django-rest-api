from cliente.models import Cliente

from django.contrib import admin


class OptionClientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_editable = ('ativo',)
    ordering = ['nome']


admin.site.register(Cliente, OptionClientes)
