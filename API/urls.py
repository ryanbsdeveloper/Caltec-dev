from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NotificaçoesView

app_name = "api"

urlpatterns = [
    path('recebendo-notificações/', NotificaçoesView.as_view()),
]
