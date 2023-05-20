
from django.urls import path , include, re_path
from .views import cadastro, cadastrados, aluno_novo
                    

urlpatterns = [
    re_path('cadastrar/', cadastro, name='aluno_cadastar'),
    re_path('cadastrados/', cadastrados, name='aluno_cadastrado'),
    re_path('aluno-novo/', aluno_novo, name='aluno_novo'),

]