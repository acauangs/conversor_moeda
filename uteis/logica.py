import requests

# API  USD-BRL,EUR-BRL,BTC-BRL

cotacoes = requests.get(
    'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()


usd = float(cotacoes["USDBRL"]["bid"])
usd_high = float(cotacoes["USDBRL"]["high"])
usd_low = float(cotacoes["USDBRL"]["low"])
eur = float(cotacoes['EURBRL']["bid"])
eur_high = float(cotacoes["EURBRL"]["high"])
eur_low = float(cotacoes["EURBRL"]["low"])
btc = float(cotacoes['BTCBRL']["bid"])
btc_high = float(cotacoes["BTCBRL"]["high"])
btc_low = float(cotacoes["BTCBRL"]["low"])

usd = "%.2f" % usd
usd_high = "%.2f" % usd_high
usd_low = "%.2f" % usd_low
eur = "%.2f" % eur
eur_high = "%.2f" % eur_high
eur_low = "%.2f" % eur_low
btc = "%.2f" % btc
btc_high = "%.2f" % btc_high
btc_low = "%.2f" % btc_low


def cotacao_usd_eur_btc():
    valores = {
        "usd": usd,
        "usd_high": usd_high,
        "usd_low": usd_low,
        "eur": eur,
        "eur_high": eur_high,
        "eur_low": eur_low,
        "btc": btc,
        "btc_high": btc_high,
        "btc_low": btc_low,
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
