# https://exchange-docs.crypto.com/exchange/v1/rest-ws/index.html?python#introduction
# Crypto.com API Docs

import requests
import json
import os
from forex_python.converter import CurrencyRates


current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "../crypto.json")

with open(json_path, "r") as f:
  config = json.load(f)

api_key = config.get("CRYPTO_COM_API_KEY")
api_secret = config.get("CRYPTO_COM_SECRET")
base_url = "https://api.crypto.com/v2" 
f.close()

def usd_to_cad(amount):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "../crypto.json")

    with open(json_path, "r") as f:
        config = json.load(f)

    api_key = config.get("CONVERSION_API_KEY")
   
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

    response = requests.get(api_url)
    data = response.json()

    cad = data['conversion_rates']['CAD']

    cad_total = float(amount) * float(cad)
    return cad_total


def check_btc_price():
   
    endpoint = "/public/get-ticker"

    params = {
        "instrument_name": "BTCUSD-PERP" 
    }

    response = requests.get(base_url + endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        #print("Response: ", data)
    else:
       print(f"Error: {response.status_code}, {response.text}")
    
    current_price = data['result']['data'][0]['a']
    cad_price = usd_to_cad(current_price)
    # print(f"USD Price: ${current_price}")
    # print(f"CAD Price: ${cad_price}")
    return cad_price

def check_sol_price():
   
    endpoint = "/public/get-ticker"

    params = {
        "instrument_name": "SOLUSD-PERP" 
    }

    response = requests.get(base_url + endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        #print("Response: ", data)
    else:
       print(f"Error: {response.status_code}, {response.text}")
    
    current_price = data['result']['data'][0]['a']
    cad_price = usd_to_cad(current_price)
    # print(f"USD Price: ${current_price}")
    # print(f"CAD Price: ${cad_price}")
    return cad_price

def check_eth_price():
   
    endpoint = "/public/get-ticker"

    params = {
        "instrument_name": "ETHUSD-PERP" 
    }

    response = requests.get(base_url + endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        #print("Response: ", data)
    else:
       print(f"Error: {response.status_code}, {response.text}")
    
    current_price = data['result']['data'][0]['a']
    cad_price = usd_to_cad(current_price)
    # print(f"USD Price: ${current_price}")
    # print(f"CAD Price: ${cad_price}")
    return cad_price
  
if __name__ == "__main__":
    print(check_btc_price())
    print(check_sol_price())
    print(check_eth_price())
   
  
  


