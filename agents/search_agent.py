import requests

class SearchAgent:

    def get_crypto_prices(self):

        print("Fetching crypto prices...")

        url = "https://api.coingecko.com/api/v3/simple/price"

        params = {
            "ids": "bitcoin,ethereum",
            "vs_currencies": "usd"
        }

        response = requests.get(url, params=params)

        data = response.json()

        bitcoin_price = data["bitcoin"]["usd"]
        ethereum_price = data["ethereum"]["usd"]

        return {
            "Bitcoin": bitcoin_price,
            "Ethereum": ethereum_price
        }