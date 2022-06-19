from ast import arg
import json
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from logs.models import Notificacoes
from .serializers import NotificaçõesSerializer
from django.contrib.auth import get_user_model


class NotificaçoesView(APIView):

    def get(self, request, *args, **kwargs):
        articles = Notificacoes.objects.all()
        return Response({"notificações": articles})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)

        return Response(f'enviado')



