from django.db import models

import datetime

year_dropdown = []

for year in reversed(range(1980, (datetime.datetime.now().year + 5))):
    year_dropdown.append((year, year))


class Veiculo(models.Model):
    modelo = models.CharField('modelo', max_length=50)
    placa = models.CharField('placa', max_length=7)
    #ano = models.IntegerField('ano',)
    ano = models.IntegerField('ano', max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
    quilometragem = models.DecimalField('Km', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.placa