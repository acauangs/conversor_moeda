import json
from turtle import onclick

import requests

# API  USD-BRL,EUR-BRL,BTC-BRL

cotacoes = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()


def cotacao_usd_eur_btc():
    valores = {
        "usd": cotacoes["USDBRL"]["bid"],
        "eur": cotacoes['EURBRL']["bid"],
        "btc": cotacoes['BTCBRL']["bid"],
    }
    return valores


def real_to_dollar(real):
    one_usd = float(cotacoes["USDBRL"]["bid"])
    real = float(real)
    if real:
        real = real / one_usd
        return "%.2f" % real
    else:
        return f'Ops.. Algo inesperado ocorreu tente novamente mais tarde :c'


def real_to_euro(real):
    one_eur = float(cotacoes['EURBRL']["bid"])
    real = float(real)
    if real:
        real = real / one_eur
        return "%.2f" % real
    else:
        return f'Ops.. Algo inesperado ocorreu tente novamente mais tarde :c'


def real_to_btc(real):
    one_btc = float(cotacoes['BTCBRL']["bid"])
    real = float(real)
    if real:
        real = real / one_btc
        return "%.2f" % real
    else:
        return f'Ops.. Algo inesperado ocorreu tente novamente mais tarde :c'
