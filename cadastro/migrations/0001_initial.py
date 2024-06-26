# Generated by Django 5.0.4 on 2024-04-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('matricula_aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=200, null=True)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('ano_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('matricula_professor', models.AutoField(primary_key=True, serialize=False)),
                ('nome_professor', models.CharField(blank=True, max_length=200, null=True)),
                ('idade_professor', models.IntegerField(blank=True, null=True)),
                ('ano_nascimento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
