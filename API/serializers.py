from rest_framework.serializers import ModelSerializer
from logs.models import Notificacoes

class NotificaçõesSerializer(ModelSerializer):

    class Meta:
        model = Notificacoes
        fields = (
            'id',
            'email',
            'notificationType',
            'notificationCode',
            )