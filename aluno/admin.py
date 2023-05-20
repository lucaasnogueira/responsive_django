from django.contrib import admin
from .models import (
    Escola,
    Serie,
    Nivel,
    Aluno,

)

class AlunoAdmin(admin.ModelAdmin):
    list_display=('id', 'nome', 'email', 'telefone')
    list_filter=('nome',)
    search_fields=('id,','nome', 'email', 'telefone')

admin.site.register(Escola)
admin.site.register(Serie)
admin.site.register(Nivel)
admin.site.register(Aluno, AlunoAdmin)