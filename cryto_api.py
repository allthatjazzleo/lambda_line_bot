import json
import requests


def coin_price(crypto_name):
  crypto_name = crypto_name.lower()
  coin_list = requests.get("https://www.cryptocompare.com/api/data/coinlist/")

  coin_lists = []
  coin_names = []
  data = coin_list.json()['Data']
  for i in data:
    
    coin_lists.append(data[i]['Name'].lower())
    coin_names.append(data[i]['CoinName'].lower())
  
  for count, item in enumerate(coin_lists):
    if crypto_name == item:
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coin_lists[count].upper()+"&tsyms=BTC,USD,HKD")
        return r.json()
    
  for count, item in enumerate(coin_names):
    if crypto_name == item:
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+coin_lists[count].upper()+"&tsyms=BTC,USD,HKD")
        return r.json()
    
  return False

