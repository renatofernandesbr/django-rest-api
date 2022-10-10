from escola.models import Aluno, Curso, Matricula
from escola.serializer import (AlunoSerializer,
                               CursoSerializer,
                               MatriculaSerializer,
                               MatriculaAlunoSerializer,
                               AlunoCursoSerializer)

from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos."""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """Exibe todos os cursos."""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """Exibe todas as matrículas."""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasAlunoAPIView(generics.ListAPIView):
    """Exibe todas as matrículas de um aluno."""

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])

    serializer_class = MatriculaAlunoSerializer


class AlunosCursoAPIView(generics.ListAPIView):
    """Exibe todos os alunos de um curso."""

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])

    serializer_class = AlunoCursoSerializer
