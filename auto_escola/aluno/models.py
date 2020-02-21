from django.db import models


STATUS_ALUNO = (('A', 'ativo'),('I', 'inativo'),)


class Aluno(models.Model):
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=200)
    email = models.CharField('email', max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_ALUNO, default='A')
    id_escola = models.IntegerField('id_escola')
    senha = models.CharField('senha', max_length=100)

    def __str__(self):
        return self.nome
