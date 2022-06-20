from rest_framework.serializers import ModelSerializer
from logs.models import NotificaçõesModel

class NotificaçõesSerializer(ModelSerializer):

    class Meta:
        model = NotificaçõesModel
        fields = (
            'id',
            'email',
            'notificationType',
            'notificationCode',
            )