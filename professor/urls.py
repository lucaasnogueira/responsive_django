from django.urls import path , include, re_path
from .views import (
    cadastro,
    cadastrados,
    professor_novo,
    professor_update,
    professor_delete,
)
                    

urlpatterns = [
    re_path('cadastrar/', cadastro, name='professor_cadastar'),
    re_path('cadastrados/', cadastrados, name='professor_cadastrado'),
    re_path('professor-novo/', professor_novo, name='professor_novo'),
    re_path('professor-update/(?P<id>\d+)/', professor_update, name='professor_update'),
    re_path('professor-delete/(?P<id>\d+)/', professor_delete, name='professor_delete'),
]