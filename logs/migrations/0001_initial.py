# Generated by Django 3.2 on 2022-06-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('cod', models.CharField(max_length=200, verbose_name='Código Transação')),
                ('cod_tipo', models.CharField(max_length=200, verbose_name='Código Transação')),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Empresa / Pessoal')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('whatsapp', models.CharField(max_length=100, unique=True, verbose_name='WhatsApp')),
                ('senha', models.CharField(max_length=200, verbose_name='Senha')),
                ('licenca', models.CharField(default='gratuita', max_length=50, null=True, verbose_name='Licença')),
                ('max_pesagens', models.CharField(default='30', max_length=10, null=True, verbose_name='Max de pesagens')),
            ],
        ),
    ]
