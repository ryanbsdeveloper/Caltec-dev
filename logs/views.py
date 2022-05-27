import email
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.messages import success, error

from .models import UsersModel
from .utils import telefone


class Help(TemplateView):
    template_name = 'help.html'
    
    def get(self, request):
        return render(request, self.template_name)


class Account(View):
    template_name = 'account.html'
    template_name_success = 'account_created.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST['nome']
        email = request.POST['email']
        tel = request.POST['telefone']
        password = request.POST['password']
        
        tel = telefone(tel)
        db_email = UsersModel.objects.filter(email=email)
        db_tel = UsersModel.objects.filter(whatsapp=tel)
        
        if db_email:
            error(request, 'Email já está em uso')
            return render(request, self.template_name)

        elif db_tel:
            error(request, 'Telefone já está em uso')
            return render(request, self.template_name)

        elif not tel:
            error(request, 'Número inválido')
            return render(request, self.template_name)
        elif len(tel) == 9:
            error(request, 'Adicione o DDD em seu número.')
            return render(request, self.template_name)

        elif len(tel) != 11:
            error(request, 'Número incompleto')
            return render(request, self.template_name)

        elif len(name) < 6:
            error(request, 'Nome da Empresa / pessoal muito curto.')
            return render(request, self.template_name)

        elif len(password) < 7:
            error(request, 'Senha muito curta.')
            return render(request, self.template_name)

        db = UsersModel(nome=name, email=email, whatsapp=tel, senha=password, licenca='free')
        db.save()
        return render(request, self.template_name_success)


class App(View):
    template_name = 'app.html'
    template_name_success = 'app_send.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
    def post(self, request, *args, **kwargs):
        context = {
            'email':request.POST['email']
        }
        email = request.POST['email']
        db = UsersModel.objects.filter(email=email)
        if db:
            '''Código pra enviar email'''
            return render(request, self.template_name_success, context)
        else:
            error(request, 'Esse e-mail não está vinculado a nenhuma conta')
            return render(request, self.template_name)

