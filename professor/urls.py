from django.urls import path , include, re_path
from .views import cadastro, cadastrados, aluno_novo
                    

urlpatterns = [
    re_path('cadastrar/', cadastro, name='professor_cadastar'),
    re_path('cadastrados/', cadastrados, name='professor_cadastrado'),
    re_path('professor-novo/', aluno_novo, name='professor_novo'),

]