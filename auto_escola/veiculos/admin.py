from django.contrib import admin
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = (
        'placa',
        'modelo',
        'quilometragem',
    )
    list_filter = ('placa', )
