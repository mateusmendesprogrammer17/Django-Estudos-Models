# Generated by Django 5.1.2 on 2024-10-16 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('carga_horaria', models.IntegerField()),
                ('data_termino', models.DateField()),
                ('duracao', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.curso'),
        ),
    ]
