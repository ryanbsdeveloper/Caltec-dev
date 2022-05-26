from django.db import models

class UsersModel(models.Model):
    nome = models.CharField(verbose_name='Nome Empresa / Pessoal', max_length=100, unique=True)
    email = models.EmailField(verbose_name='Email', max_length=100, unique=True)
    whatsapp = models.CharField(verbose_name='WhatsApp', max_length=100)
    senha = models.CharField(verbose_name='Senha', max_length=200)
    licenca = models.CharField(verbose_name="Licença", default='gratuita', null=True, max_length=50)

    def __str__(self) -> str:
        return self.email