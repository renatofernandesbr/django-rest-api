from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=11, default='')
    foto = models.ImageField(upload_to='escola', blank=True)

    def __str__(self):
        return f'{self.nome}'


class Curso(models.Model):
    NIVEIS = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo = models.CharField(max_length=10, blank=False, null=False)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEIS, blank=False, null=False, default='B')

    def __str__(self):
        return f'{self.codigo} - {self.descricao}'


class Matricula(models.Model):
    TURNOS = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length=1, choices=TURNOS, blank=False, null=False, default='M')

    def __str__(self):
        return f'{self.curso.codigo} - {self.aluno.nome}'
