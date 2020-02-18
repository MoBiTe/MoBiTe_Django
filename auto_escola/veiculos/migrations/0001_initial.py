# Generated by Django 3.0.3 on 2020-02-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='modelo')),
                ('placa', models.CharField(max_length=7, verbose_name='placa')),
                ('ano', models.IntegerField(max_length=4, verbose_name='ano')),
                ('quilometragem', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Km')),
            ],
        ),
    ]
