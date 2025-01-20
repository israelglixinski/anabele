import requests
import json

def get_dollar_quote():
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    response = requests.get(url)
    datar = response.json()
    dollar_exchange = datar['USDBRL']['bid']
    return float(dollar_exchange)


