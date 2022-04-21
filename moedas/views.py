from re import A

from django.shortcuts import render
from uteis.logica import cotacao_usd_eur_btc, real_to_dollar

# Create your views here.


def home(request):
    valor_real = request.GET.get('q')
    if valor_real:
        context = {
            'valor': cotacao_usd_eur_btc,
            'valor_real': real_to_dollar(valor_real),
        }
        return render(request, 'moedas/pages/home.html', context)

    else:
        context = {
            'valor': cotacao_usd_eur_btc,
        }
        return render(request, 'moedas/pages/home.html', context)
