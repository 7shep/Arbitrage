# https://exchange-docs.crypto.com/exchange/v1/rest-ws/index.html?python#introduction
# Crypto.com API Docs

import requests
import json
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "../crypto.json")

with open(json_path, "r") as f:
  config = json.load(f)

api_key = config.get("CRYPTO_COM_API_KEY")
api_secret = config.get("CRYPTO_COM_SECRET")
base_url = "https://api.crypto.com/v2" 
f.close()



