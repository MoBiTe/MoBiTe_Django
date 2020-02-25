from django.contrib import admin
from .models import Aula


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = (
        'aluno_id',
        'automovel_id',
        'data_aula',
        'hora_aula',
    )
    list_filter = ('aluno_id', )
    date_hierarchy = 'data_aula'
