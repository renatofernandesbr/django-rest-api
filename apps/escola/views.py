from escola.models import Aluno, Curso, Matricula
from escola.serializer import (AlunoSerializer,
                               AlunoSerializerV2,
                               CursoSerializer,
                               MatriculaSerializer,
                               MatriculaAlunoSerializer,
                               AlunoCursoSerializer)

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.serializers import Serializer


@staticmethod
def create_serializer_class(serializer_class, request) -> Serializer:
    if not issubclass(serializer_class, Serializer):
        raise APIException(f'O serializador {serializer_class} não é uma'
                           'subclasse de rest_framework.serializers.Serializer.')
    return serializer_class(data=request.data)  # pylint: disable=not-callable


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos."""

    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2

        return AlunoSerializer

    def create(self, request, *args, **kwargs) -> Response | None:
        serializer_class = self.get_serializer_class()
        serializer = create_serializer_class(serializer_class, request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            identifier = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + identifier
            return response
        return None


class CursosViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """Exibe todos os cursos."""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = []
    permission_classes = []
    pagination_class = None

    def create(self, request, *args, **kwargs) -> Response | None:
        serializer = create_serializer_class(self.get_serializer_class(), request)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            identifier = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + identifier
            return response
        return None


class MatriculasViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """Exibe todas as matrículas."""

    http_method_names = ['get', 'post']

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasAlunoAPIView(generics.ListAPIView):
    """Exibe todas as matrículas de um aluno."""

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])

    serializer_class = MatriculaAlunoSerializer


class AlunosCursoAPIView(generics.ListAPIView):
    """Exibe todos os alunos de um curso."""

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])

    serializer_class = AlunoCursoSerializer
