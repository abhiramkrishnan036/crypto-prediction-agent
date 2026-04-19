class PredictionAgent:

    def predict_next_move(self, historical_data):

        print("Analyzing historical data...")

        first_price = historical_data[0]
        last_price = historical_data[-1]

        if last_price > first_price:
            prediction = "UP"
        else:
            prediction = "DOWN"

        return prediction