# Generated by Django 3.0.3 on 2020-02-25 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_auto_20200221_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='email',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='id_escola',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='telefone',
        ),
    ]
