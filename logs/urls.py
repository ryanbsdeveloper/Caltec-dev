from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Help.as_view(), name='help'),
    path('conta/', views.Account.as_view(), name='account')
    path('app/', views.App.as_view(), name='app'),
]
