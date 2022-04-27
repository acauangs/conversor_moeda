from django.urls import path

from . import views

urlpatterns = [
    path('', views.cotacao, name='cotacao'),
    path('converte/usd', views.converter_usd, name='converter_usd'),
    path('converte/eur', views.converter_eur, name='converter_eur'),
    path('converte/btc', views.converter_btc, name='converter_btc'),
]
