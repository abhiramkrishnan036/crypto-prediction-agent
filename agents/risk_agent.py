class RiskAgent:

    def calculate_risk(self, probability, odds):

        print("Calculating risk using Kelly Criterion...")

        q = 1 - probability

        kelly_fraction = (odds * probability - q) / odds

        if kelly_fraction < 0:
            kelly_fraction = 0

        return round(kelly_fraction, 2)