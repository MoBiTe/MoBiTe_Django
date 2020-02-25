from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'cpf',
        'status',
    )
    search_fields = ('nome', )
    list_filter = ('status', )
