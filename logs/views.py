from django.shortcuts import render
from django.views.generic import TemplateView, View


class Help(TemplateView):
    template_name = 'help.html'
    
    def get(self, request):
        return render(request, self.template_name)

class Account(View):
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, args, **kwargs):
        pass

class App(View):
    template_name = 'app.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
    def post(self, request, args, **kwargs):
        pass