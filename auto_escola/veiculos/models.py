from django.db import models

import datetime

year_dropdown = []

for year in reversed(range(1980, (datetime.datetime.now().year + 5))):
    year_dropdown.append((year, year))


class Veiculo(models.Model):
    placa = models.CharField('placa', max_length=7)
    fabricante = models.CharField('fabricante', max_length=50)
    modelo = models.CharField('modelo', max_length=50)
    ano_fabricacao = models.IntegerField('ano de fabricação', max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
    ano_modelo = models.IntegerField('ano do modelo', max_length=4, choices=year_dropdown, default=datetime.datetime.now().year)
    quilometragem = models.DecimalField('Km', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.placa