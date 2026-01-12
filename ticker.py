import requests
import time

def get_crypto_price(crypto_id):
    # Using CoinGecko API (No API key needed for basic use)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        price = data[crypto_id]['usd']
        return price
    except Exception as e:
        return f"Error: {e}"

print("--- Live Crypto Ticker (Press Ctrl+C to stop) ---")

while True:
    # You can change 'bitcoin' to 'ethereum' or 'solana'
    btc_price = get_crypto_price('bitcoin')
    eth_price = get_crypto_price('ethereum')
    
    print(f"BTC: ${btc_price} | ETH: ${eth_price}")
    
    # Wait 10 seconds before checking again to avoid being banned by the API
    time.sleep(10)
    