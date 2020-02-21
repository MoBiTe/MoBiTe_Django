from django.db import models
import time


class Aula(models.Model):
    escola_id = models.IntegerField('ID Escola')
    aluno_id = models.IntegerField('ID Aluno')
    instrutor_id = models.IntegerField('ID Instrutor')
    automovel_id = models.IntegerField('ID Automóvel')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    '''
    def __str__(self):
        return self
    '''