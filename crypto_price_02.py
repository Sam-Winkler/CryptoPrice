import requests
import tkinter as tk
import time


# Create a function to get the current price of a cryptocurrency
def get_crypto_price(crypto_id):
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
        )
        response.raise_for_status()
        crypto_price = response.json()[crypto_id]["usd"]
        return crypto_price
    except requests.exceptions.RequestException:
        print(f"Request for price failed. Retrying in 5 seconds...")
        time.sleep(5)
        return get_crypto_price(crypto_id)


def display_price(currency):
    print("")
    print(currency + ": $" + str(get_crypto_price(currency)))
    print("")


currencies = ["ethereum", "solana", "polkadot"]
for currency in currencies:
    display_price(currency)

val = input("You good, bro?")
