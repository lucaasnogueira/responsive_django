from django.contrib import admin
from .models import (
    Faculdade,
    Curso,
    Período,
    Professor,

)

class ProfessorAdmin(admin.ModelAdmin):
    list_display=('id', 'nome', 'email', 'telefone')
    list_filter=('nome','faculdade','periodo')
    search_fields=('id,','nome', 'email', 'telefone')

admin.site.register(Faculdade)
admin.site.register(Curso)
admin.site.register(Período)
admin.site.register(Professor, ProfessorAdmin)