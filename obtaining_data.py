import requests
import json

# def get_dollar_quote():
#     url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
#     response = requests.get(url)
#     datar = response.json()
#     print(datar)
#     dollar_exchange = datar['USDBRL']['bid']
#     return float(dollar_exchange)

def get_dollar_quote():
    url = 'https://api.exchangerate.fun/latest?base=USD'
    response = requests.get(url)
    data = response.json()
    return float(data['rates']['BRL'])


if __name__ == '__main__':
    get_dollar_quote()


    pass