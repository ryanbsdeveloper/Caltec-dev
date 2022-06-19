from django.db import models

class UsersModel(models.Model):
    nome = models.CharField(verbose_name='Nome Empresa / Pessoal', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)
    whatsapp = models.CharField(verbose_name='WhatsApp', max_length=100, unique=True)
    senha = models.CharField(verbose_name='Senha', max_length=200)
    licenca = models.CharField(verbose_name="Licença", default='gratuita', null=True, max_length=50)
    max_pesagens = models.CharField(verbose_name='Max de pesagens', default='30', null=True, max_length=10)

    def __str__(self) -> str:
        return self.email

class Notificacoes(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=100, unique=True, null=True)
    notificationCode = models.CharField(verbose_name='Código Notificação', max_length=200,null=True)
    notificationType = models.CharField(verbose_name='Tipo do código', max_length=200,null=True)


