import requests
import datetime


def get_humans():
    api = requests.get("https://api.poh.dev/status")
    data = api.json()
    return data["registry"]["registered"]


def get_pending_humans():
    api = requests.get("https://api.poh.dev/status")
    data = api.json()
    return data["registry"]["pending_registration"]["total"]


def get_price():
    api = requests.get(
        "https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xdd1ad9a21ce722c151a836373babe42c868ce9a4&vs_currencies=usd&include_24hr_change=true")
    data = api.json()
    return data['0xdd1ad9a21ce722c151a836373babe42c868ce9a4']["usd"]


def get_24hs_variation():
    api = requests.get(
        "https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xdd1ad9a21ce722c151a836373babe42c868ce9a4&vs_currencies=usd&include_24hr_change=true")
    data = api.json()
    return data['0xdd1ad9a21ce722c151a836373babe42c868ce9a4']["usd_24h_change"]


def get_time():
    time = datetime.datetime.now()
    return time.strftime("%H-%M")


horas = ["02-00","03-00","04-00","05-00","06-00","07-00","08-00","09-00","10-00","11-00","12-00","13-00","14-00","15-00","16-00","17-00","18-00","19-00","20-00","21-00","22-00","23-00","24-00"]
horas_2 = ["08-00","14-00","20-00"]