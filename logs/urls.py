from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('/', views, name='account'),
    path('app/', views, name='app'),
    path('help/', views, name='help')
]
