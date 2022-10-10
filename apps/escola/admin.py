from escola.models import Aluno, Curso, Matricula

from django.contrib import admin


class OptionAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ['nome']
    search_fields = ['nome']
    ordering = ['nome']


class OptionCursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ['codigo']
    search_fields = ['codigo', 'descricao']
    ordering = ['codigo']


class OptionMatriculas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'aluno', 'turno')
    list_display_links = ['id']
    ordering = ['curso__codigo', 'aluno__nome']


admin.site.register(Aluno, OptionAlunos)
admin.site.register(Curso, OptionCursos)
admin.site.register(Matricula, OptionMatriculas)
