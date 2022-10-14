import os
import random

from faker import Faker
from validate_docbr import CPF

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from escola.models import Aluno, Curso # pylint: disable=wrong-import-position

def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        rg = (f'{random.randrange(10, 99)}{random.randrange(100, 999)}'  # pylint: disable=invalid-name
              f'{random.randrange(100, 999)}{random.randrange(0, 9)}')
        cpf = cpf.generate()
        data_nascimento = fake.date_between(start_date='-18y', end_date='today')
        aluno = Aluno(nome=nome, rg=rg, cpf=cpf, data_nascimento=data_nascimento)
        aluno.save()


def criando_cursos(quantidade_de_cursos):
    for _ in range(quantidade_de_cursos):
        codigo_curso = (f'{random.choice("ABCDEF")}{random.randrange(10, 99)}-'
                        f'{random.randrange(1, 9)}')
        descs = ['Python Fundamentos',
                 'Python intermediário',
                 'Python Avançado',
                 'Python para Data Science', 'Python/React']
        descricao = random.choice(descs)
        descs.remove(descricao)
        nivel = random.choice("BIA")
        curso = Curso(codigo=codigo_curso, descricao=descricao, nivel=nivel)
        curso.save()


criando_alunos(200)
criando_cursos(5)
