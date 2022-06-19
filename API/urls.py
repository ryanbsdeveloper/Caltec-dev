from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import NotificaçoesView

app_name = "api"

urlpatterns = [
    path('api/', NotificaçoesView.as_view()),
]
