from escola.models import Aluno, Curso, Matricula

from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto']


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'celular', 'foto']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class MatriculaAlunoSerializer(serializers.ModelSerializer):
    def get_turno(self, obj):
        return obj.get_turno_display()

    curso = serializers.ReadOnlyField(source='curso.codigo')
    turno = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'turno']


class AlunoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['aluno']
        depth = 1
