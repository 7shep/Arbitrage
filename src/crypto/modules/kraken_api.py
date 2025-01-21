import krakenex

def check_btc_price():
    api = krakenex.API()

    response = api.query_public('Ticker', {'pair': 'XBTCAD'})

    if response.get('error'):
        print(f"Error:", response['error'])
    else:
        ticker = response['result']['XXBTZCAD']
        last_trade_price = ticker['c'][0]
        print(f"Latest BTC Price (CAD): ${last_trade_price}")

def check_eth_price():
    api = krakenex.API()

    response = api.query_public('Ticker', {'pair': 'XETHZCAD'})

    if response.get('error'):
        print(f"Error:", response['error'])
    else:
        ticker = response['result']['XETHZCAD']
        last_trade_price = ticker['c'][0]
        print(f"Latest ETH Price (CAD): ${last_trade_price}")

def check_sol_price():
    api = krakenex.API()

    response = api.query_public('Ticker', {'pair': 'SOLCAD'})

    if response.get('error'):
        print(f"Error:", response['error'])
    else:
        ticker = response['result']['SOLCAD']
        last_trade_price = ticker['c'][0]
        print(f"Latest SOL Price (CAD): ${last_trade_price}")


if __name__ == "__main__":
    check_btc_price()
    check_eth_price()
    check_sol_price()