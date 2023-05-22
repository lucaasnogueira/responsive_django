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
    professores = Professor.objects.all()
    return render(request, 'cadastrados_professores.html', {'professores':professores })

def professor_novo(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('professor_cadastrado')


def professor_update(request, id):
    data ={}
    professor = Professor.objects.get(id=id)
    form = ProfessorForm(request.POST or None, instance=professor)
    data['professor'] = professor
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('professor_cadastrado')
    else:
        return render(request, 'update_professor.html', data)
 
def professor_delete(request, id):
    professor = Professor.objects.get(id=id)
    if request.method == 'POST':
        professor.delete()
        return redirect('professor_cadastrado')
    else:
        return render(request, 'delete_confirm.html', {'professor':professor})
