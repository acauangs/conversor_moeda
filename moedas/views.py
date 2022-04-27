from re import A

from django.shortcuts import render
from uteis.logica import *

# Create your views here.


def cotacao(request):
    context = {
        'valor': cotacao_usd_eur_btc,
    }

    return render(request, 'moedas/pages/cotacao.html', context)


def converter_usd(request):
    valor_real = request.GET.get('q')
    if valor_real:
        context = {
            'valor_real': real_to_dollar(valor_real),
            'dollar': 'UDS:'
        }
        return render(request, 'moedas/pages/converter_usd.html', context)

    return render(request, 'moedas/pages/converter_usd.html')


def converter_eur(request):
    valor_real = request.GET.get('q')
    if valor_real:
        context = {
            'valor_real': real_to_euro(valor_real),
            'euro': 'EUR'
        }
        return render(request, 'moedas/pages/converter_eur.html', context)

    return render(request, 'moedas/pages/converter_eur.html')


def converter_btc(request):
    valor_real = request.GET.get('q')
    if valor_real:
        context = {
            'valor_real': real_to_btc(valor_real),
            'bitcoin': 'BTC'
        }
        return render(request, 'moedas/pages/converter_btc.html', context)

    return render(request, 'moedas/pages/converter_btc.html')
