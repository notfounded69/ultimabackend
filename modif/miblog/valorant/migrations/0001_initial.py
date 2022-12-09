# Generated by Django 2.1.7 on 2022-12-09 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre Agente')),
                ('detail', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='projects')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='F.Public')),
            ],
            options={
                'verbose_name': 'Agente',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('descr', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='F. Agreg')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='F. Actz')),
            ],
            options={
                'verbose_name': 'Role',
            },
        ),
        migrations.CreateModel(
            name='formBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('correo', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Registro',
            },
        ),
        migrations.AddField(
            model_name='agentes',
            name='categor',
            field=models.ManyToManyField(to='valorant.Categoria', verbose_name='rol'),
        ),
    ]
