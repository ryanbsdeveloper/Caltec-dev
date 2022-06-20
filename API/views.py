from rest_framework.views import APIView
from rest_framework.response import Response
from logs.models import NotificaçõesModel
from rest_framework.permissions import BasePermission
from .serializers import NotificaçõesSerializer

'''
['DATA', 'FILES', 'POST', 'QUERY_PARAMS', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
  '_auth', '_authenticate', '_authenticator', '_content_type', '_data', '_default_negotiator',
   '_files', '_full_data', '_load_data_and_files', '_load_stream', '_not_authenticated', '_parse',
    '_request', '_stream', '_supports_form_parsing', '_user', 'accepted_media_type', 'accepted_renderer',
     'auth', 'authenticators', 'content_type', 'data', 'force_plaintext_errors', 'method', 'negotiator', 
     'parser_context', 'parsers', 'query_params', 'stream', 'successful_authenticator', 'user', 'version', 
     'versioning_scheme']
'''



class NotificaçoesView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('As notificações não serão exibidas aqui.')

    def post(self, request, *args, **kwargs):
        if 'notificationCode' not in request.POST:
            return Response(f'Não foi possível adicionar essa notificação')

        code = request.POST['notificationCode']
        tipo = request.POST['notificationType']
        db = NotificaçõesModel(notificationCode=code, notificationType=tipo)
        db.save()

        return Response(f'Notificação adicionada')
