from modules import kraken_api, coinbase_api, crypto_com_api

while True:
    # Store the prices in variables for ETH, SOL, and BTC
    kraken_eth = kraken_api.check_eth_price()
    crypto_com_eth = crypto_com_api.check_eth_price()
    coinbase_eth = coinbase_api.check_eth_price()

    kraken_sol = kraken_api.check_sol_price()
    crypto_com_sol = crypto_com_api.check_sol_price()
    coinbase_sol = coinbase_api.check_sol_price()

    kraken_btc = kraken_api.check_btc_price()
    crypto_com_btc = crypto_com_api.check_btc_price()
    coinbase_btc = coinbase_api.check_btc_price()

    # Print the prices in the desired order (ETH, SOL, BTC)
    print(f"Kraken ETH Price: ${kraken_eth}")
    print(f"Crypto.Com ETH Price: ${crypto_com_eth}")
    print(f"Coinbase ETH Price: ${coinbase_eth}")
    
    print(f"Kraken SOL Price: ${kraken_sol}")
    print(f"Crypto.Com SOL Price: ${crypto_com_sol}")
    print(f"Coinbase SOL Price: ${coinbase_sol}")
    
    print(f"Kraken BTC Price: ${kraken_btc}")
    print(f"Crypto.Com BTC Price: ${crypto_com_btc}")
    print(f"Coinbase BTC Price: ${coinbase_btc}")
