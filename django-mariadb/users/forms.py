from django import forms

from .models import Aluno


class AlunosForm(forms.ModelForm):
    class Meta:
          model = Aluno
          fields = ['nome','email']