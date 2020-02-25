from django.db import models


STATUS_ALUNO = (('A', 'ativo'),('I', 'inativo'),)


class Aluno(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    status = models.CharField(max_length=1, choices=STATUS_ALUNO, default='A')

    def __str__(self):
        return self.nome
