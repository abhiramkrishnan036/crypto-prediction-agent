import random

class DataFetchAgent:

    def get_historical_data(self):

        print("Fetching historical crypto data...")

        data = []

        for i in range(1000):
            price = random.uniform(20000, 80000)
            data.append(price)

        return data