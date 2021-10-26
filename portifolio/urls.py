from os import name
from django.urls import path
from . import views

app_name = 'portifolio'

urlpatterns = [
    path('', views.index, name='index'),
]