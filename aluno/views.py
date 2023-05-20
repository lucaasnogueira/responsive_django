from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlunoForm
from .models import Aluno


# Create your views here.
def cadastro (request):
    form = AlunoForm()
    data = {'form': form}
    return render(request, 'cadastro_aluno.html', data)

def cadastrados (request):
    alunos = Aluno.objects.all()
    return render(request, 'cadastrados_alunos.html', {'alunos':alunos })

def aluno_novo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('aluno_cadastrado')

