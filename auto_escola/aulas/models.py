from django.db import models
from auto_escola.aluno.models import Aluno
from auto_escola.veiculos.models import Veiculo

import datetime


class Aula(models.Model):
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, default=None)
    # automovel_id = models.IntegerField('ID Automóvel')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, default=None)
    data_aula = models.DateField('Data', default=datetime.date.today)
    hora_aula = models.TimeField('Hora de início', default=datetime.datetime.now)
