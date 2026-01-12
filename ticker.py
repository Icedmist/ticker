import requests
import time
from datetime import datetime

# this is the confirguration
# you can add as many coins as you want here (use their CoinGecko IDs) which can be found from coingeicko.com
# e.g., 'binancecoin', 'matic-network', 'shiba-inu'
watchlist = ['bitcoin', 'ethereum', 'solana', 'ripple', 'cardano', 'dogecoin']

def get_prices(coins):
    # Join list into a string: "bitcoin,ethereum,solana"
    ids = ",".join(coins)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Server returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

print(f"--- thinking... Tracking {len(watchlist)} Pairs (Press Ctrl+C to stop) ---")

while True:
    data = get_prices(watchlist)
    
    if data:
        # Get current time for the log
        now = datetime.now().strftime("%H:%M:%S")
        print(f"\n[{now}] Market Update:")
        
        # Loop through the watchlist to print them in order
        for coin in watchlist:
            if coin in data:
                price = data[coin]['usd']
                # The {:<12} part just formats the text to align nicely
                print(f"{coin.capitalize():<12} : ${price:,}") 
            else:
                print(f"{coin:<12} : (No Data)")
    
    # Refresh every 15 seconds
    time.sleep(15)
    