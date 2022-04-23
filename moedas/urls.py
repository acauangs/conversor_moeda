from django.urls import path

from . import views

urlpatterns = [
    path('', views.cotacao, name='cotacao'),
    path('converte/usd', views.converter_usd, name='converter_usd'),
]
