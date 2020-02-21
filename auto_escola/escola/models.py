from django.db import models


class Escola(models.Model):
    nome_fantasia = models.CharField('Nome Fantasia', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereco', max_length=200)
    email = models.CharField('email', max_length=100)

    def __str__(self):
        return self.nome_fantasia
