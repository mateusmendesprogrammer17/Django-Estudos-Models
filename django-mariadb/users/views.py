from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlunosForm
from .models import Aluno,Curso
from django.db.models import Count

def home(request):
    if request.method == 'POST':
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a mesma página após salvar o formulário
    else:
        form = AlunosForm()  # Cria um formulário vazio para GET

    return render(request, 'users/index.html', {'form': form})

def lista_alunos(request):
    alunos = Aluno.objects.all()  # Carregar alunos dentro da função
    return render(request, 'users/lista_alunos.html', {'alunos': alunos})

def cursos(request):
    cursos = Curso.objects.annotate(qtd_alunos=Count('alunos')).all()
    return render(request,'users/lista_cursos.html',{'cursos':cursos})

from django.shortcuts import render
from .models import Aluno

def whatCourse(request):
    try:
        students = Aluno.objects.all().select_related('curso')
    except Exception as e:
        # Log a mensagem de erro ou tratar a exceção conforme necessário
        students = []  # Ou lidar de outra forma

    return render(request, 'users/whatcourse.html', {
        'students': students,
        'total_students': students.count(),
    })
