from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfessorForm
from .models import Professor


# Create your views here.
def cadastro (request):
    form = ProfessorForm()
    data = {'form': form}
    return render(request, 'cadastro_professor.html', data)

def cadastrados (request):
    professor = Professor.objects.all()
    return render(request, 'cadastrados_professores.html', {'professor':professor })

def aluno_novo(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('professor_cadastrado')

