# Generated by Django 5.0.4 on 2024-04-11 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_nota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='nota',
        ),
        migrations.AddField(
            model_name='nota',
            name='nota1',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota2',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota3',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
        migrations.AddField(
            model_name='nota',
            name='nota4',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
