# Generated by Django 3.0.3 on 2020-02-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(max_length=100, verbose_name='nome')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('telefone', models.CharField(max_length=11, verbose_name='telefone')),
                ('endereco', models.CharField(max_length=200, verbose_name='endereco')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
            ],
        ),
    ]
