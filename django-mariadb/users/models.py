from django.db import models

# Create your models here.


# relação curso e aluno 
#  1 para n 
#  muitos alunos frequentam um curso e um curso pode ter mais de um aluno

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    description = models.TextField()
    carga_horaria = models.IntegerField() #quantidade de horas
    data_termino=models.DateField()
    duracao = models.CharField(max_length=50) # duracao = models.CharField(max_length=50)  # por exemplo, "6 semanas"
   
    def __str__(self):
        return self.nome
class Aluno(models.Model):
    nome = models.CharField(max_length=100 , null=False) # not null e varchar(100)
    email = models.EmailField(max_length=150,unique=True) # unique
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE, null=True,related_name='alunos')
    
    def __str__(self):
        return self.nome 
