from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlunosForm
from .models import Aluno

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
    return HttpResponse("Cursos")
