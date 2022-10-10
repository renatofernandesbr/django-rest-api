from escola.views import (AlunosViewSet,
                          CursosViewSet,
                          MatriculasViewSet,
                          MatriculasAlunoAPIView,
                          AlunosCursoAPIView)

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', MatriculasAlunoAPIView.as_view()),
    path('curso/<int:pk>/alunos/', AlunosCursoAPIView.as_view()),
]
