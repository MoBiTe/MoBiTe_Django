from django.db import models
import datetime


class Aula(models.Model):
    aluno_id = models.IntegerField('ID Aluno')
    automovel_id = models.IntegerField('ID Automóvel')
    data_aula = models.DateField('Data', default=datetime.date.today)
    hora_aula = models.TimeField('Hora de início', default=datetime.datetime.now)
