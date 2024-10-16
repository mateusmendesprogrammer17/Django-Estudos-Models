
from django.urls import path
from users.views import home, lista_alunos,cursos  # Importe a view home também

urlpatterns = [

    path('', home, name='home'),  # URL para a homepage
    path('alunos/', lista_alunos, name='alunos'),
    path('cursos/', cursos, name='cursos'),# URL para a página de perfil
]
