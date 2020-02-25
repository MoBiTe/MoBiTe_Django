from django.contrib import admin
from .models import Aula


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'nome_aluno',
        'veiculo',
        'data_aula',
        'hora_aula',
    )
    list_filter = ('nome_aluno', )
    date_hierarchy = 'data_aula'
